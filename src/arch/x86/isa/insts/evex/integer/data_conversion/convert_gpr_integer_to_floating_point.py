microcode = '''
def macroop EVEX_VCVTSI2SS_XMM_XMM_R {
    gem5_avx_cvtsi32n64_ss xmm1, xmm2, regm, srcSize=dsz, destSize=4, ext=XMM
};

def macroop EVEX_VCVTSI2SS_XMM_XMM_M {
    ld t1, seg, sib, disp, dataSize=4
    gem5_avx_cvtsi32n64_ss xmm1, xmm2, t1, srcSize=dsz, destSize=4, ext=XMM
};

def macroop EVEX_VCVTSI2SS_XMM_XMM_P {
    rdip t7
    ld t1, seg, riprel, disp, dataSize=4
    gem5_avx_cvtsi32n64_ss xmm1, xmm2, t1, srcSize=dsz, destSize=4, ext=XMM
};

def macroop EVEX_VCVTSI2SD_XMM_XMM_R {
    gem5_avx_cvtsi32n64_sd xmm1, xmm2, regm, srcSize=dsz, destSize=8, ext=XMM
};

def macroop EVEX_VCVTSI2SD_XMM_XMM_M {
    ld t1, seg, sib, disp, dataSize=8
    gem5_avx_cvtsi32n64_sd xmm1, xmm2, t1, srcSize=dsz, destSize=8, ext=XMM
};

def macroop EVEX_VCVTSI2SD_XMM_XMM_P {
    rdip t7
    ld t1, seg, riprel, disp, dataSize=8
    gem5_avx_cvtsi32n64_sd xmm1, xmm2, t1, srcSize=dsz, destSize=8, ext=XMM
};

def macroop EVEX_VCVTUSI2SS_XMM_XMM_R {
    gem5_avx_cvtsu32n64_ss xmm1, xmm2, regm, srcSize=dsz, destSize=4, ext=XMM
};

def macroop EVEX_VCVTUSI2SS_XMM_XMM_M {
    ld t1, seg, sib, disp, dataSize=4
    gem5_avx_cvtsu32n64_ss xmm1, xmm2, t1, srcSize=dsz, destSize=4, ext=XMM
};

def macroop EVEX_VCVTUSI2SS_XMM_XMM_P {
    rdip t7
    ld t1, seg, riprel, disp, dataSize=4
    gem5_avx_cvtsu32n64_ss xmm1, xmm2, t1, srcSize=dsz, destSize=4, ext=XMM
};

def macroop EVEX_VCVTUSI2SD_XMM_XMM_R {
    gem5_avx_cvtsu32n64_sd xmm1, xmm2, regm, srcSize=dsz, destSize=8, ext=XMM
};

def macroop EVEX_VCVTUSI2SD_XMM_XMM_M {
    ld t1, seg, sib, disp, dataSize=8
    gem5_avx_cvtsu32n64_sd xmm1, xmm2, t1, srcSize=dsz, destSize=8, ext=XMM
};

def macroop EVEX_VCVTUSI2SD_XMM_XMM_P {
    rdip t7
    ld t1, seg, riprel, disp, dataSize=8
    gem5_avx_cvtsu32n64_sd xmm1, xmm2, t1, srcSize=dsz, destSize=8, ext=XMM
};

'''
