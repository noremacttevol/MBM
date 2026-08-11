import subprocess, numpy as np, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
V2 = os.path.dirname(HERE)

def load_mono_from_mp4(mp4, af=None, sr=44100):
    cmd = ['ffmpeg','-v','quiet','-i',mp4]
    if af:
        cmd += ['-af', af]
    cmd += ['-ac','1','-ar',str(sr),'-f','f32le','-']
    p = subprocess.run(cmd, capture_output=True)
    return np.frombuffer(p.stdout, dtype=np.float32)

def voiced_spectrum(x, sr=44100, nfft=4096):
    hop=nfft//2
    frames=[x[i:i+nfft] for i in range(0,len(x)-nfft,hop)]
    frames=[f for f in frames if len(f)==nfft]
    rms=np.array([np.sqrt(np.mean(f**2)) for f in frames])
    thr=np.percentile(rms[rms>1e-4], 40) if (rms>1e-4).any() else 0
    win=np.hanning(nfft)
    acc=np.zeros(nfft//2+1); n=0
    for f,r in zip(frames,rms):
        if r>=thr and r>1e-4:
            S=np.abs(np.fft.rfft(f*win))**2
            acc+=S; n+=1
    acc/=max(n,1)
    freqs=np.fft.rfftfreq(nfft,1/sr)
    return freqs, acc

def band_db(freqs, spec, lo, hi):
    m=(freqs>=lo)&(freqs<hi)
    return 10*np.log10(spec[m].mean()+1e-20)

bands=[(300,1000),(1000,3000),(3000,6000),(6000,10000),(10000,16000)]

def tilt(mp4, af=None):
    x=load_mono_from_mp4(mp4, af)
    f,s=voiced_spectrum(x)
    ref=band_db(f,s,300,1000)
    return [band_db(f,s,lo,hi)-ref for lo,hi in bands]

approved={'50':os.path.join(V2,'build-50-noblemans-son/john-4_noblemans-son.mp4'),
          '70':os.path.join(V2,'build-70-temptations/matt-4_the-temptations.mp4'),
          '97':os.path.join(V2,'build-97-the-empty-tomb/luke-24_the-empty-tomb.mp4')}
row27=os.path.join(V2,'build-27-leaven/matthew-13_leaven.mp4')

appr_tilt=np.mean([tilt(v) for v in approved.values()], axis=0)

candidate = sys.argv[1] if len(sys.argv)>1 else None
t27 = tilt(row27, candidate)
print(f"filter: {candidate}")
print(f"{'band':>12} {'r27+eq':>9} {'appr':>9} {'delta':>8}")
for i,(lo,hi) in enumerate(bands):
    d = t27[i]-appr_tilt[i]
    flag = " MUFFLED" if d<-2 else (" bright" if d>2 else " OK")
    print(f"{lo}-{hi:>6} {t27[i]:9.2f} {appr_tilt[i]:9.2f} {d:+8.2f}{flag}")
