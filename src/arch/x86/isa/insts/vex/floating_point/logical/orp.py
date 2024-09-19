microcode = '''
def macroop VEX_VORPS_XMM_XMM_XMM {
    gem5_avx_or_epu32 xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop VEX_VORPS_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_or_epu32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VORPS_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_or_epu32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VORPS_YMM_YMM_YMM {
    gem5_avx_or_epu32 ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop VEX_VORPS_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_or_epu32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VORPS_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_or_epu32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VORPD_XMM_XMM_XMM {
    gem5_avx_or_epu64 xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop VEX_VORPD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_or_epu64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VORPD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_or_epu64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VORPD_YMM_YMM_YMM {
    gem5_avx_or_epu64 ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop VEX_VORPD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_or_epu64 ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop VEX_VORPD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_or_epu64 ymm1, ymm2, uvec1, size=8, ext=YMM
};
'''
