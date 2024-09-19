microcode = '''
def macroop VEX_VCVTDQ2PS_XMM_XMM {
    gem5_avx_cvtepi32_ps xmm, xmmm, size=4, ext=XMM
};

def macroop VEX_VCVTDQ2PS_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtepi32_ps xmm, uvec1, size=4, ext=XMM
};

def macroop VEX_VCVTDQ2PS_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_cvtepi32_ps xmm, uvec1, size=4, ext=XMM
};

def macroop VEX_VCVTDQ2PS_YMM_YMM {
    gem5_avx_cvtepi32_ps ymm, ymmm, size=4, ext=YMM
};

def macroop VEX_VCVTDQ2PS_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_cvtepi32_ps ymm, uvec1, size=4, ext=YMM
};

def macroop VEX_VCVTDQ2PS_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_cvtepi32_ps ymm, uvec1, size=4, ext=YMM
};

def macroop VEX_VCVTDQ2PD_XMM_XMM {
    gem5_avx_cvtepi32_pd xmm, xmmm, srcSize=4, destSize=8, ext=XMM
};

def macroop VEX_VCVTDQ2PD_XMM_M {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    gem5_avx_cvtepi32_pd xmm, uvec1, srcSize=4, destSize=8, ext=XMM
};

def macroop VEX_VCVTDQ2PD_XMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_cvtepi32_pd xmm, uvec1, srcSize=4, destSize=8, ext=XMM
};

def macroop VEX_VCVTDQ2PD_YMM_XMM {
    gem5_avx_cvtepi32_pd ymm, xmmm, srcSize=4, destSize=8, ext=YMM
};

def macroop VEX_VCVTDQ2PD_YMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_cvtepi32_pd ymm, uvec1, srcSize=4, destSize=8, ext=YMM
};

def macroop VEX_VCVTDQ2PD_YMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_cvtepi32_pd ymm, uvec1, srcSize=4, destSize=8, ext=YMM
};

'''
