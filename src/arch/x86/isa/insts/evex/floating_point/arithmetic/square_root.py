microcode = '''
def macroop EVEX_VSQRTSS_XMM_XMM_XMM {
    gem5_avx_sqrt_ss xmm1, xmm2, xmmm, size=4, ext=Scalar
};

def macroop EVEX_VSQRTSS_XMM_XMM_M {
    gem5_mm_load_ss uvec1, seg, sib, disp, dataSize=4
    gem5_avx_sqrt_ss xmm1, xmm2, uvec1, size=4, ext=Scalar
};

def macroop EVEX_VSQRTSS_XMM_XMM_P {
    rdip t7
    gem5_mm_load_ss uvec1, seg, riprel, disp, dataSize=4
    gem5_avx_sqrt_ss xmm1, xmm2, uvec1, size=4, ext=Scalar
};

def macroop EVEX_VSQRTSD_XMM_XMM_XMM {
    gem5_avx_sqrt_sd xmm1, xmm2, xmmm, size=8, ext=Scalar
};

def macroop EVEX_VSQRTSD_XMM_XMM_M {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    gem5_avx_sqrt_sd xmm1, xmm2, uvec1, size=8, ext=Scalar
};

def macroop EVEX_VSQRTSD_XMM_XMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_sqrt_sd xmm1, xmm2, uvec1, size=8, ext=Scalar
};

def macroop EVEX_VSQRTPS_XMM_XMM {
    gem5_avx_sqrt_ps xmm, xmmm, size=4, ext=XMM
};

def macroop EVEX_VSQRTPS_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_sqrt_ps xmm, uvec1, size=4, ext=XMM
};

def macroop EVEX_VSQRTPS_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_sqrt_ps xmm, uvec1, size=4, ext=XMM
};

def macroop EVEX_VSQRTPS_YMM_YMM {
    gem5_avx_sqrt_ps ymm, ymmm, size=4, ext=YMM
};

def macroop EVEX_VSQRTPS_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_sqrt_ps ymm, uvec1, size=4, ext=YMM
};

def macroop EVEX_VSQRTPS_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_sqrt_ps ymm, uvec1, size=4, ext=YMM
};

def macroop EVEX_VSQRTPS_ZMM_ZMM {
    gem5_avx_sqrt_ps zmm, zmmm, size=4, ext=ZMM
};

def macroop EVEX_VSQRTPS_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_sqrt_ps zmm, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VSQRTPS_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_sqrt_ps zmm, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VSQRTPD_XMM_XMM {
    gem5_avx_sqrt_pd xmm, xmmm, size=8, ext=XMM
};

def macroop EVEX_VSQRTPD_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_sqrt_pd xmm, uvec1, size=8, ext=XMM
};

def macroop EVEX_VSQRTPD_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_sqrt_pd xmm, uvec1, size=8, ext=XMM
};

def macroop EVEX_VSQRTPD_YMM_YMM {
    gem5_avx_sqrt_pd ymm, ymmm, size=8, ext=YMM
};

def macroop EVEX_VSQRTPD_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_sqrt_pd ymm, uvec1, size=8, ext=YMM
};

def macroop EVEX_VSQRTPD_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_sqrt_pd ymm, uvec1, size=8, ext=YMM
};

def macroop EVEX_VSQRTPD_ZMM_ZMM {
    gem5_avx_sqrt_pd zmm, zmmm, size=8, ext=ZMM
};

def macroop EVEX_VSQRTPD_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_sqrt_pd zmm, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VSQRTPD_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_sqrt_pd zmm, uvec1, size=8, ext=ZMM
};
'''
