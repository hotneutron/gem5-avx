microcode = '''
def macroop EVEX_VCVTDQ2PS_XMM_XMM {
    gem5_avx_cvtepi32_ps xmm, xmmm, size=4, ext=XMM
};

def macroop EVEX_VCVTDQ2PS_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtepi32_ps xmm, uvec1, size=4, ext=XMM
};

def macroop EVEX_VCVTDQ2PS_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtepi32_ps xmm, uvec1, size=4, ext=XMM
};

def macroop EVEX_VCVTDQ2PS_YMM_YMM {
    gem5_avx_cvtepi32_ps ymm, ymmm, size=4, ext=YMM
};

def macroop EVEX_VCVTDQ2PS_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_cvtepi32_ps ymm, uvec1, size=4, ext=YMM
};

def macroop EVEX_VCVTDQ2PS_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_cvtepi32_ps ymm, uvec1, size=4, ext=YMM
};

def macroop EVEX_VCVTDQ2PS_ZMM_ZMM {
    gem5_avx_cvtepi32_ps zmm, zmmm, size=4, ext=ZMM
};

def macroop EVEX_VCVTDQ2PS_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_cvtepi32_ps zmm, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VCVTDQ2PS_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_cvtepi32_ps zmm, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VCVTDQ2PD_XMM_XMM {
    gem5_avx_cvtepi32_pd xmm, xmmm, srcSize=4, destSize=8, ext=XMM
};

def macroop EVEX_VCVTDQ2PD_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_cvtepi32_pd xmm, uvec1, srcSize=4, destSize=8, ext=XMM
};

def macroop EVEX_VCVTDQ2PD_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_cvtepi32_pd xmm, uvec1, srcSize=4, destSize=8, ext=XMM
};

def macroop EVEX_VCVTDQ2PD_YMM_XMM {
    gem5_avx_cvtepi32_pd ymm, xmmm, srcSize=4, destSize=8, ext=YMM
};

def macroop EVEX_VCVTDQ2PD_YMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_cvtepi32_pd ymm, uvec1, srcSize=4, destSize=8, ext=YMM
};

def macroop EVEX_VCVTDQ2PD_YMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_cvtepi32_pd ymm, uvec1, srcSize=4, destSize=8, ext=YMM
};

def macroop EVEX_VCVTDQ2PD_ZMM_YMM {
    gem5_avx_cvtepi32_pd zmm, ymmm, srcSize=4, destSize=8, ext=ZMM
};

def macroop EVEX_VCVTDQ2PD_ZMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_cvtepi32_pd zmm, uvec1, srcSize=4, destSize=8, ext=ZMM
};

def macroop EVEX_VCVTDQ2PD_ZMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_cvtepi32_pd zmm, uvec1, srcSize=4, destSize=8, ext=ZMM
};

def macroop EVEX_VCVTUDQ2PS_XMM_XMM {
    gem5_avx_cvtepu32_ps xmm, xmmm, size=4, ext=XMM
};

def macroop EVEX_VCVTUDQ2PS_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtepu32_ps xmm, uvec1, size=4, ext=XMM
};

def macroop EVEX_VCVTUDQ2PS_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtepu32_ps xmm, uvec1, size=4, ext=XMM
};

def macroop EVEX_VCVTUDQ2PS_YMM_YMM {
    gem5_avx_cvtepu32_ps ymm, ymmm, size=4, ext=YMM
};

def macroop EVEX_VCVTUDQ2PS_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_cvtepu32_ps ymm, uvec1, size=4, ext=YMM
};

def macroop EVEX_VCVTUDQ2PS_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_cvtepu32_ps ymm, uvec1, size=4, ext=YMM
};

def macroop EVEX_VCVTUDQ2PS_ZMM_ZMM {
    gem5_avx_cvtepu32_ps zmm, zmmm, size=4, ext=ZMM
};

def macroop EVEX_VCVTUDQ2PS_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_cvtepu32_ps zmm, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VCVTUDQ2PS_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_cvtepu32_ps zmm, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VCVTUDQ2PD_XMM_XMM {
    gem5_avx_cvtepu32_pd xmm, xmmm, srcSize=4, destSize=8, ext=XMM
};

def macroop EVEX_VCVTUDQ2PD_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_cvtepu32_pd xmm, uvec1, srcSize=4, destSize=8, ext=XMM
};

def macroop EVEX_VCVTUDQ2PD_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_cvtepu32_pd xmm, uvec1, srcSize=4, destSize=8, ext=XMM
};

def macroop EVEX_VCVTUDQ2PD_YMM_XMM {
    gem5_avx_cvtepu32_pd ymm, xmmm, srcSize=4, destSize=8, ext=YMM
};

def macroop EVEX_VCVTUDQ2PD_YMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_cvtepu32_pd ymm, uvec1, srcSize=4, destSize=8, ext=YMM
};

def macroop EVEX_VCVTUDQ2PD_YMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_cvtepu32_pd ymm, uvec1, srcSize=4, destSize=8, ext=YMM
};

def macroop EVEX_VCVTUDQ2PD_ZMM_YMM {
    gem5_avx_cvtepu32_pd zmm, ymmm, srcSize=4, destSize=8, ext=ZMM
};

def macroop EVEX_VCVTUDQ2PD_ZMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_cvtepu32_pd zmm, uvec1, srcSize=4, destSize=8, ext=ZMM
};

def macroop EVEX_VCVTUDQ2PD_ZMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_cvtepu32_pd zmm, uvec1, srcSize=4, destSize=8, ext=ZMM
};

'''
