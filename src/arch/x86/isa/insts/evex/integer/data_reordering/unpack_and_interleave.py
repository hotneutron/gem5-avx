microcode = '''
def macroop EVEX_VPUNPCKLDQ_XMM_XMM_XMM {
    gem5_avx_unpacklo_epu32 xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop EVEX_VPUNPCKLDQ_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_unpacklo_epu32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VPUNPCKLDQ_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_unpacklo_epu32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VPUNPCKLDQ_YMM_YMM_YMM {
    gem5_avx_unpacklo_epu32 ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop EVEX_VPUNPCKLDQ_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_unpacklo_epu32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPUNPCKLDQ_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_unpacklo_epu32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPUNPCKLDQ_ZMM_ZMM_ZMM {
    gem5_avx_unpacklo_epu32 zmm1, zmm2, zmmm, size=4, ext=ZMM
};

def macroop EVEX_VPUNPCKLDQ_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, disp, dataSize=64
    gem5_avx_unpacklo_epu32 zmm1, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPUNPCKLDQ_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, disp, dataSize=64
    gem5_avx_unpacklo_epu32 zmm1, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPUNPCKLQDQ_XMM_XMM_XMM {
    gem5_avx_unpacklo_epu64 xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop EVEX_VPUNPCKLQDQ_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_unpacklo_epu64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VPUNPCKLQDQ_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_unpacklo_epu64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VPUNPCKLQDQ_YMM_YMM_YMM {
    gem5_avx_unpacklo_epu64 ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop EVEX_VPUNPCKLQDQ_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_unpacklo_epu64 ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VPUNPCKLQDQ_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_unpacklo_epu64 ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VPUNPCKLQDQ_ZMM_ZMM_ZMM {
    gem5_avx_unpacklo_epu64 zmm1, zmm2, zmmm, size=8, ext=ZMM
};

def macroop EVEX_VPUNPCKLQDQ_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, disp, dataSize=64
    gem5_avx_unpacklo_epu64 zmm1, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VPUNPCKLQDQ_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, disp, dataSize=64
    gem5_avx_unpacklo_epu64 zmm1, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VPUNPCKHDQ_XMM_XMM_XMM {
    gem5_avx_unpackhi_epu32 xmm1, xmm2, xmmm, ext=0, size=4
};

def macroop EVEX_VPUNPCKHDQ_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_unpackhi_epu32 xmm1, xmm2, uvec1, ext=0, size=4
};

def macroop EVEX_VPUNPCKHDQ_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_unpackhi_epu32 xmm1, xmm2, uvec1, ext=0, size=4
};

def macroop EVEX_VPUNPCKHDQ_YMM_YMM_YMM {
    gem5_avx_unpackhi_epu32 ymm1, ymm2, ymmm, ext=1, size=4
};

def macroop EVEX_VPUNPCKHDQ_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_unpackhi_epu32 ymm1, ymm2, uvec1, ext=1, size=4
};

def macroop EVEX_VPUNPCKHDQ_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_unpackhi_epu32 ymm1, ymm2, uvec1, ext=1, size=4
};

def macroop EVEX_VPUNPCKHDQ_ZMM_ZMM_ZMM {
    gem5_avx_unpackhi_epu32 zmm1, zmm2, zmmm, ext=1, size=4
};

def macroop EVEX_VPUNPCKHDQ_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, disp, dataSize=64
    gem5_avx_unpackhi_epu32 zmm1, zmm2, uvec1, ext=1, size=4
};

def macroop EVEX_VPUNPCKHDQ_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, disp, dataSize=64
    gem5_avx_unpackhi_epu32 zmm1, zmm2, uvec1, ext=1, size=4
};

def macroop EVEX_VPUNPCKHQDQ_XMM_XMM_XMM {
    gem5_avx_unpackhi_epu64 xmm1, xmm2, xmmm, ext=0, size=8
};

def macroop EVEX_VPUNPCKHQDQ_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_unpackhi_epu64 xmm1, xmm2, uvec1, ext=0, size=8
};

def macroop EVEX_VPUNPCKHQDQ_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=16
    gem5_avx_unpackhi_epu64 xmm1, xmm2, uvec1, ext=0, size=8
};

def macroop EVEX_VPUNPCKHQDQ_YMM_YMM_YMM {
    gem5_avx_unpackhi_epu64 ymm1, ymm2, ymmm, ext=1, size=8
};

def macroop EVEX_VPUNPCKHQDQ_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_unpackhi_epu64 ymm1, ymm2, uvec1, ext=1, size=8
};

def macroop EVEX_VPUNPCKHQDQ_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, disp, dataSize=32
    gem5_avx_unpackhi_epu64 ymm1, ymm2, uvec1, ext=1, size=8
};

def macroop EVEX_VPUNPCKHQDQ_ZMM_ZMM_ZMM {
    gem5_avx_unpackhi_epu64 zmm1, zmm2, zmmm, ext=1, size=8
};

def macroop EVEX_VPUNPCKHQDQ_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, disp, dataSize=64
    gem5_avx_unpackhi_epu64 zmm1, zmm2, uvec1, ext=1, size=8
};

def macroop EVEX_VPUNPCKHQDQ_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, disp, dataSize=64
    gem5_avx_unpackhi_epu64 zmm1, zmm2, uvec1, ext=1, size=8
};

'''
