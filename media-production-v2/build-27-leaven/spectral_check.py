import subprocess, numpy as np, sys

def load_mono(mp4, sr=44100):
    p = subprocess.run(['ffmpeg','-v','quiet','-i',mp4,'-ac','1','-ar',str(sr),'-f','f32le','-'],
                       capture_output=True)
    return np.frombuffer(p.stdout, dtype=np.float32)

def voiced_spectrum(x, sr=44100, nfft=4096):
    # frame, keep voiced frames (RMS above 20th pct of active), average power spectrum
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

rows={'27':'build-27-leaven/matthew-13_leaven.mp4',
      '50':'build-50-noblemans-son/john-4_noblemans-son.mp4',
      '70':'build-70-temptations/matt-4_the-temptations.mp4',
      '97':'build-97-the-empty-tomb/luke-24_the-empty-tomb.mp4'}
bands=[(300,1000),(1000,3000),(3000,6000),(6000,10000),(10000,16000)]
res={}
for k,v in rows.items():
    x=load_mono(v)
    f,s=voiced_spectrum(x)
    # normalize to the 300-1000 band (speech fundamental region) so we compare TILT not loudness
    ref=band_db(f,s,300,1000)
    res[k]=[band_db(f,s,lo,hi)-ref for lo,hi in bands]

print("Band tilt (dB, normalized to 300-1000Hz band=0):")
print(f"{'band':>12} " + " ".join(f"{k:>8}" for k in rows))
appr=['50','70','97']
for i,(lo,hi) in enumerate(bands):
    label=f"{lo//1000 if lo>=1000 else lo}-{hi//1000}k"
    line=f"{label:>12} " + " ".join(f"{res[k][i]:8.2f}" for k in rows)
    print(line)
print()
print("Row27 vs approved-mean (negative = row27 DARKER/muffled):")
for i,(lo,hi) in enumerate(bands):
    am=np.mean([res[k][i] for k in appr])
    d=res['27'][i]-am
    label=f"{lo}-{hi}Hz"
    flag=" <== MUFFLED" if d<-3 else (" <== bright" if d>3 else "")
    print(f"  {label:>14}: {d:+6.2f} dB{flag}")
