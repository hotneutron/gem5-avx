microcode = '''
def macroop EVEX_VPANDD_XMM_XMM_XMM {
    gem5_avx_and_epu32 xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop EVEX_VPANDD_XMM_XMM_M {
    lea t1,  seg, sib, disp, dataSize=asz
    ldvec128 uvec1, seg, [1, t0, t1], dataSize=16
    gem5_avx_and_epu32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VPANDD_XMM_XMM_P {
    rdip t7
    lea t1,  seg, riprel, disp, dataSize=asz
    ldvec128 uvec1, seg, [1, t0, t1], dataSize=16
    gem5_avx_and_epu32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VPANDD_YMM_YMM_YMM {
    gem5_avx_and_epu32 ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop EVEX_VPANDD_YMM_YMM_M {
    lea t1,  seg, sib, disp, dataSize=asz
    ldvec256 uvec1, seg, [1, t0, t1], dataSize=32
    gem5_avx_and_epu32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPANDD_YMM_YMM_P {
    rdip t7
    lea t1, seg, riprel, disp, dataSize=asz
    ldvec256 uvec1, seg, [1, t0, t1], dataSize=32
    gem5_avx_and_epu32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPANDD_ZMM_ZMM_ZMM {
    gem5_avx_and_epu32 zmm1, zmm2, zmmm, size=4, ext=ZMM
};

def macroop EVEX_VPANDD_ZMM_ZMM_M {
    lea t1,  seg, sib, disp, dataSize=asz
    ldvec512 uvec1, seg, [1, t0, t1], dataSize=64
    gem5_avx_and_epu32 zmm1, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPANDD_ZMM_ZMM_P {
    rdip t7
    lea t1, seg, riprel, disp, dataSize=asz
    ldvec512 uvec1, seg, [1, t0, t1], dataSize=64
    gem5_avx_and_epu32 zmm1, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPANDQ_XMM_XMM_XMM {
    gem5_avx_and_epu64 xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop EVEX_VPANDQ_XMM_XMM_M {
    lea t1,  seg, sib, disp, dataSize=asz
    ldvec128 uvec1, seg, [1, t0, t1], dataSize=16
    gem5_avx_and_epu64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VPANDQ_XMM_XMM_P {
    rdip t7
    lea t1,  seg, riprel, disp, dataSize=asz
    ldvec128 uvec1, seg, [1, t0, t1], dataSize=16
    gem5_avx_and_epu64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VPANDQ_YMM_YMM_YMM {
    gem5_avx_and_epu64 ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop EVEX_VPANDQ_YMM_YMM_M {
    lea t1,  seg, sib, disp, dataSize=asz
    ldvec256 uvec1, seg, [1, t0, t1], dataSize=32
    gem5_avx_and_epu64 ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VPANDQ_YMM_YMM_P {
    rdip t7
    lea t1, seg, riprel, disp, dataSize=asz
    ldvec256 uvec1, seg, [1, t0, t1], dataSize=32
    gem5_avx_and_epu64 ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VPANDQ_ZMM_ZMM_ZMM {
    gem5_avx_and_epu64 zmm1, zmm2, zmmm, size=8, ext=ZMM
};

def macroop EVEX_VPANDQ_ZMM_ZMM_M {
    lea t1,  seg, sib, disp, dataSize=asz
    ldvec512 uvec1, seg, [1, t0, t1], dataSize=64
    gem5_avx_and_epu64 zmm1, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VPANDQ_ZMM_ZMM_P {
    rdip t7
    lea t1, seg, riprel, disp, dataSize=asz
    ldvec512 uvec1, seg, [1, t0, t1], dataSize=64
    gem5_avx_and_epu64 zmm1, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VPANDND_XMM_XMM_XMM {
    gem5_avx_andn_epu32 xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop EVEX_VPANDND_XMM_XMM_M {
    lea t1,  seg, sib, disp, dataSize=asz
    ldvec128 uvec1, seg, [1, t0, t1], dataSize=16
    gem5_avx_andn_epu32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VPANDND_XMM_XMM_P {
    rdip t7
    lea t1,  seg, riprel, disp, dataSize=asz
    ldvec128 uvec1, seg, [1, t0, t1], dataSize=16
    gem5_avx_andn_epu32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VPANDND_YMM_YMM_YMM {
    gem5_avx_andn_epu32 ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop EVEX_VPANDND_YMM_YMM_M {
    lea t1,  seg, sib, disp, dataSize=asz
    ldvec256 uvec1, seg, [1, t0, t1], dataSize=32
    gem5_avx_andn_epu32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPANDND_YMM_YMM_P {
    rdip t7
    lea t1, seg, riprel, disp, dataSize=asz
    ldvec256 uvec1, seg, [1, t0, t1], dataSize=32
    gem5_avx_andn_epu32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPANDND_ZMM_ZMM_ZMM {
    gem5_avx_andn_epu32 zmm1, zmm2, zmmm, size=4, ext=ZMM
};

def macroop EVEX_VPANDND_ZMM_ZMM_M {
    lea t1,  seg, sib, disp, dataSize=asz
    ldvec512 uvec1, seg, [1, t0, t1], dataSize=64
    gem5_avx_andn_epu32 zmm1, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPANDND_ZMM_ZMM_P {
    rdip t7
    lea t1, seg, riprel, disp, dataSize=asz
    ldvec512 uvec1, seg, [1, t0, t1], dataSize=64
    gem5_avx_andn_epu32 zmm1, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPANDNQ_XMM_XMM_XMM {
    gem5_avx_andn_epu64 xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop EVEX_VPANDNQ_XMM_XMM_M {
    lea t1,  seg, sib, disp, dataSize=asz
    ldvec128 uvec1, seg, [1, t0, t1], dataSize=16
    gem5_avx_andn_epu64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VPANDNQ_XMM_XMM_P {
    rdip t7
    lea t1,  seg, riprel, disp, dataSize=asz
    ldvec128 uvec1, seg, [1, t0, t1], dataSize=16
    gem5_avx_andn_epu64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VPANDNQ_YMM_YMM_YMM {
    gem5_avx_andn_epu64 ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop EVEX_VPANDNQ_YMM_YMM_M {
    lea t1,  seg, sib, disp, dataSize=asz
    ldvec256 uvec1, seg, [1, t0, t1], dataSize=32
    gem5_avx_andn_epu64 ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VPANDNQ_YMM_YMM_P {
    rdip t7
    lea t1, seg, riprel, disp, dataSize=asz
    ldvec256 uvec1, seg, [1, t0, t1], dataSize=32
    gem5_avx_andn_epu64 ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VPANDNQ_ZMM_ZMM_ZMM {
    gem5_avx_andn_epu64 zmm1, zmm2, zmmm, size=8, ext=ZMM
};

def macroop EVEX_VPANDNQ_ZMM_ZMM_M {
    lea t1,  seg, sib, disp, dataSize=asz
    ldvec512 uvec1, seg, [1, t0, t1], dataSize=64
    gem5_avx_andn_epu64 zmm1, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VPANDNQ_ZMM_ZMM_P {
    rdip t7
    lea t1, seg, riprel, disp, dataSize=asz
    ldvec512 uvec1, seg, [1, t0, t1], dataSize=64
    gem5_avx_andn_epu64 zmm1, zmm2, uvec1, size=8, ext=ZMM
};

'''
