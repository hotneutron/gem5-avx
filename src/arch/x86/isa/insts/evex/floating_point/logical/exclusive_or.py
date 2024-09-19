microcode = '''
def macroop EVEX_VXORPS_XMM_XMM_XMM {
    gem5_avx_xor_epu32 xmm1, xmm2, xmmm, size=16, ext=XMM
};

def macroop EVEX_VXORPS_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_xor_epu32 xmm1, xmm2, uvec1, size=16, ext=XMM
};

def macroop EVEX_VXORPS_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_xor_epu32 xmm1, xmm2, uvec1, size=16, ext=XMM
};

def macroop EVEX_VXORPS_YMM_YMM_YMM {
    gem5_avx_xor_epu32 ymm1, ymm2, ymmm, size=32, ext=YMM
};

def macroop EVEX_VXORPS_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_xor_epu32 ymm1, ymm2, uvec1, size=32, ext=YMM
};

def macroop EVEX_VXORPS_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_xor_epu32 ymm1, ymm2, uvec1, size=32, ext=YMM
};

def macroop EVEX_VXORPS_ZMM_ZMM_ZMM {
    gem5_avx_xor_epu32 zmm1, zmm2, zmmm, size=32, ext=ZMM
};

def macroop EVEX_VXORPS_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, disp, dataSize=64
    gem5_avx_xor_epu32 zmm1, zmm2, uvec1, size=64, ext=ZMM
};

def macroop EVEX_VXORPS_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, disp, dataSize=64
    gem5_avx_xor_epu32 zmm1, zmm2, uvec1, size=64, ext=ZMM
};

def macroop EVEX_VXORPD_XMM_XMM_XMM {
    gem5_avx_xor_epu64 xmm1, xmm2, xmmm, size=16, ext=XMM
};

def macroop EVEX_VXORPD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_xor_epu64 xmm1, xmm2, uvec1, size=16, ext=XMM
};

def macroop EVEX_VXORPD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_xor_epu64 xmm1, xmm2, uvec1, size=16, ext=XMM
};

def macroop EVEX_VXORPD_YMM_YMM_YMM {
    gem5_avx_xor_epu64 ymm1, ymm2, ymmm, size=32, ext=YMM
};

def macroop EVEX_VXORPD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_xor_epu64 ymm1, ymm2, uvec1, size=32, ext=YMM
};

def macroop EVEX_VXORPD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_xor_epu64 ymm1, ymm2, uvec1, size=32, ext=YMM
};

def macroop EVEX_VXORPD_ZMM_ZMM_ZMM {
    gem5_avx_xor_epu64 zmm1, zmm2, zmmm, size=32, ext=ZMM
};

def macroop EVEX_VXORPD_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, disp, dataSize=64
    gem5_avx_xor_epu64 zmm1, zmm2, uvec1, size=64, ext=ZMM
};

def macroop EVEX_VXORPD_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, disp, dataSize=64
    gem5_avx_xor_epu64 zmm1, zmm2, uvec1, size=64, ext=ZMM
};
'''
