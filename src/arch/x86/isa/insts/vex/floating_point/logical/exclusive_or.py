microcode = '''
def macroop VEX_VXORPS_XMM_XMM_XMM {
    gem5_avx_xor_epu32 xmm1, xmm2, xmmm, size=16, ext=XMM
};

def macroop VEX_VXORPS_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_xor_epu32 xmm1, xmm2, uvec1, size=16, ext=XMM
};

def macroop VEX_VXORPS_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_xor_epu32 xmm1, xmm2, uvec1, size=16, ext=XMM
};

def macroop VEX_VXORPS_YMM_YMM_YMM {
    gem5_avx_xor_epu32 ymm1, ymm2, ymmm, size=32, ext=YMM
};

def macroop VEX_VXORPS_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_xor_epu32 ymm1, ymm2, uvec1, size=32, ext=YMM
};

def macroop VEX_VXORPS_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_xor_epu32 ymm1, ymm2, uvec1, size=32, ext=YMM
};

def macroop VEX_VXORPD_XMM_XMM_XMM {
    gem5_avx_xor_epu64 xmm1, xmm2, xmmm, size=16, ext=XMM
};

def macroop VEX_VXORPD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_xor_epu64 xmm1, xmm2, uvec1, size=16, ext=XMM
};

def macroop VEX_VXORPD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_xor_epu64 xmm1, xmm2, uvec1, size=16, ext=XMM
};

def macroop VEX_VXORPD_YMM_YMM_YMM {
    gem5_avx_xor_epu64 ymm1, ymm2, ymmm, size=32, ext=YMM
};

def macroop VEX_VXORPD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_xor_epu64 ymm1, ymm2, uvec1, size=32, ext=YMM
};

def macroop VEX_VXORPD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_xor_epu64 ymm1, ymm2, uvec1, size=32, ext=YMM
};
'''
