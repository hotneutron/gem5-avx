microcode = '''
def macroop VEX_VPSUBB_XMM_XMM_XMM {
    gem5_avx_sub_epu8 xmm1, xmm2, xmmm, size=1, ext=XMM
};

def macroop VEX_VPSUBB_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_sub_epu8 xmm1, xmm2, uvec1, size=1, ext=XMM
};

def macroop VEX_VPSUBB_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_sub_epu8 xmm1, xmm2, uvec1, size=1, ext=XMM
};

def macroop VEX_VPSUBB_YMM_YMM_YMM {
    gem5_avx_sub_epu8 ymm1, ymm2, ymmm, size=1, ext=YMM
};

def macroop VEX_VPSUBB_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_sub_epu8 ymm1, ymm2, uvec1, size=1, ext=YMM
};

def macroop VEX_VPSUBB_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_sub_epu8 ymm1, ymm2, uvec1, size=1, ext=YMM
};

def macroop VEX_VPSUBD_XMM_XMM_XMM {
    gem5_avx_sub_epu32 xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop VEX_VPSUBD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_sub_epu32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VPSUBD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_sub_epu32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VPSUBD_YMM_YMM_YMM {
    gem5_avx_sub_epu32 ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop VEX_VPSUBD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_sub_epu32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VPSUBD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_sub_epu32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VPSUBQ_XMM_XMM_XMM {
    gem5_avx_sub_epu64 xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop VEX_VPSUBQ_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_sub_epu64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VPSUBQ_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_sub_epu64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VPSUBQ_YMM_YMM_YMM {
    gem5_avx_sub_epu64 ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop VEX_VPSUBQ_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_sub_epu64 ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop VEX_VPSUBQ_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_sub_epu64 ymm1, ymm2, uvec1, size=8, ext=YMM
};
'''
