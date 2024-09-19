microcode = '''
def macroop EVEX_VPXORD_XMM_XMM_XMM {
    gem5_avx_xor_epu32 xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop EVEX_VPXORD_XMM_XMM_M {
    lea t1,  seg, sib, disp, dataSize=asz
    ldvec128 uvec1, seg, [1, t0, t1], dataSize=16
    gem5_avx_xor_epu32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VPXORD_XMM_XMM_P {
    rdip t7
    lea t1,  seg, riprel, disp, dataSize=asz
    ldvec128 uvec1, seg, [1, t0, t1], dataSize=16
    gem5_avx_xor_epu32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VPXORD_YMM_YMM_YMM {
    gem5_avx_xor_epu32 ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop EVEX_VPXORD_YMM_YMM_M {
    lea t1,  seg, sib, disp, dataSize=asz
    ldvec256 uvec1, seg, [1, t0, t1], dataSize=32
    gem5_avx_xor_epu32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPXORD_YMM_YMM_P {
    rdip t7
    lea t1, seg, riprel, disp, dataSize=asz
    ldvec256 uvec1, seg, [1, t0, t1], dataSize=32
    gem5_avx_xor_epu32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPXORD_ZMM_ZMM_ZMM {
    gem5_avx_xor_epu32 zmm1, zmm2, zmmm, size=4, ext=ZMM
};

def macroop EVEX_VPXORD_ZMM_ZMM_M {
    lea t1,  seg, sib, disp, dataSize=asz
    ldvec512 uvec1, seg, [1, t0, t1], dataSize=64
    gem5_avx_xor_epu32 zmm1, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPXORD_ZMM_ZMM_P {
    rdip t7
    lea t1, seg, riprel, disp, dataSize=asz
    ldvec512 uvec1, seg, [1, t0, t1], dataSize=64
    gem5_avx_xor_epu32 zmm1, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPXORQ_XMM_XMM_XMM {
    gem5_avx_xor_epu64 xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop EVEX_VPXORQ_XMM_XMM_M {
    lea t1,  seg, sib, disp, dataSize=asz
    ldvec128 uvec1, seg, [1, t0, t1], dataSize=16
    gem5_avx_xor_epu64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VPXORQ_XMM_XMM_P {
    rdip t7
    lea t1,  seg, riprel, disp, dataSize=asz
    ldvec128 uvec1, seg, [1, t0, t1], dataSize=16
    gem5_avx_xor_epu64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VPXORQ_YMM_YMM_YMM {
    gem5_avx_xor_epu64 ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop EVEX_VPXORQ_YMM_YMM_M {
    lea t1,  seg, sib, disp, dataSize=asz
    ldvec256 uvec1, seg, [1, t0, t1], dataSize=32
    gem5_avx_xor_epu64 ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VPXORQ_YMM_YMM_P {
    rdip t7
    lea t1, seg, riprel, disp, dataSize=asz
    ldvec256 uvec1, seg, [1, t0, t1], dataSize=32
    gem5_avx_xor_epu64 ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VPXORQ_ZMM_ZMM_ZMM {
    gem5_avx_xor_epu64 zmm1, zmm2, zmmm, size=8, ext=ZMM
};

def macroop EVEX_VPXORQ_ZMM_ZMM_M {
    lea t1,  seg, sib, disp, dataSize=asz
    ldvec512 uvec1, seg, [1, t0, t1], dataSize=64
    gem5_avx_xor_epu64 zmm1, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VPXORQ_ZMM_ZMM_P {
    rdip t7
    lea t1, seg, riprel, disp, dataSize=asz
    ldvec512 uvec1, seg, [1, t0, t1], dataSize=64
    gem5_avx_xor_epu64 zmm1, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VPXORD_XMM_XMM_XMM_K {
    gem5_mask_xor_epu32 xmm1, xmm2, xmmm, xmm1, opmask=opmask, size=4, ext=XMM
};

def macroop EVEX_VPXORD_XMM_XMM_M_K {
    lea t1,  seg, sib, disp, dataSize=asz
    ldvec128 uvec1, seg, [1, t0, t1], dataSize=16
    gem5_mask_xor_epu32 xmm1, xmm2, uvec1, xmm1, opmask=opmask, size=4, ext=XMM
};

def macroop EVEX_VPXORD_XMM_XMM_P_K {
    rdip t7
    lea t1,  seg, riprel, disp, dataSize=asz
    ldvec128 uvec1, seg, [1, t0, t1], dataSize=16
    gem5_mask_xor_epu32 xmm1, xmm2, uvec1, xmm1, opmask=opmask, size=4, ext=XMM
};

def macroop EVEX_VPXORD_YMM_YMM_YMM_K {
    gem5_mask_xor_epu32 ymm1, ymm2, ymmm, ymm1, opmask=opmask, size=4, ext=YMM
};

def macroop EVEX_VPXORD_YMM_YMM_M_K {
    lea t1,  seg, sib, disp, dataSize=asz
    ldvec256 uvec1, seg, [1, t0, t1], dataSize=32
    gem5_mask_xor_epu32 ymm1, ymm2, uvec1, ymm1, opmask=opmask, size=4, ext=YMM
};

def macroop EVEX_VPXORD_YMM_YMM_P_K {
    rdip t7
    lea t1, seg, riprel, disp, dataSize=asz
    ldvec256 uvec1, seg, [1, t0, t1], dataSize=32
    gem5_mask_xor_epu32 ymm1, ymm2, uvec1, ymm1, opmask=opmask, size=4, ext=YMM
};

def macroop EVEX_VPXORD_ZMM_ZMM_ZMM_K {
    gem5_mask_xor_epu32 zmm1, zmm2, zmmm, zmm1, opmask=opmask, size=4, ext=ZMM
};

def macroop EVEX_VPXORD_ZMM_ZMM_M_K {
    lea t1,  seg, sib, disp, dataSize=asz
    ldvec512 uvec1, seg, [1, t0, t1], dataSize=64
    gem5_mask_xor_epu32 zmm1, zmm2, uvec1, zmm1, opmask=opmask, size=4, ext=ZMM
};

def macroop EVEX_VPXORD_ZMM_ZMM_P_K {
    rdip t7
    lea t1, seg, riprel, disp, dataSize=asz
    ldvec512 uvec1, seg, [1, t0, t1], dataSize=64
    gem5_mask_xor_epu32 zmm1, zmm2, uvec1, zmm1, opmask=opmask, size=4, ext=ZMM
};

def macroop EVEX_VPXORQ_XMM_XMM_XMM_K {
    gem5_mask_xor_epu64 xmm1, xmm2, xmmm, xmm1, opmask=opmask, size=8, ext=XMM
};

def macroop EVEX_VPXORQ_XMM_XMM_M_K {
    lea t1,  seg, sib, disp, dataSize=asz
    ldvec128 uvec1, seg, [1, t0, t1], dataSize=16
    gem5_mask_xor_epu64 xmm1, xmm2, uvec1, xmm1, opmask=opmask, size=8, ext=XMM
};

def macroop EVEX_VPXORQ_XMM_XMM_P_K {
    rdip t7
    lea t1,  seg, riprel, disp, dataSize=asz
    ldvec128 uvec1, seg, [1, t0, t1], dataSize=16
    gem5_mask_xor_epu64 xmm1, xmm2, uvec1, xmm1, opmask=opmask, size=8, ext=XMM
};

def macroop EVEX_VPXORQ_YMM_YMM_YMM_K {
    gem5_mask_xor_epu64 ymm1, ymm2, ymmm, ymm1, opmask=opmask, size=8, ext=YMM
};

def macroop EVEX_VPXORQ_YMM_YMM_M_K {
    lea t1,  seg, sib, disp, dataSize=asz
    ldvec256 uvec1, seg, [1, t0, t1], dataSize=32
    gem5_mask_xor_epu64 ymm1, ymm2, uvec1, ymm1, opmask=opmask, size=8, ext=YMM
};

def macroop EVEX_VPXORQ_YMM_YMM_P_K {
    rdip t7
    lea t1, seg, riprel, disp, dataSize=asz
    ldvec256 uvec1, seg, [1, t0, t1], dataSize=32
    gem5_mask_xor_epu64 ymm1, ymm2, uvec1, ymm1, opmask=opmask, size=8, ext=YMM
};

def macroop EVEX_VPXORQ_ZMM_ZMM_ZMM_K {
    gem5_mask_xor_epu64 zmm1, zmm2, zmmm, zmm1, opmask=opmask, size=8, ext=ZMM
};

def macroop EVEX_VPXORQ_ZMM_ZMM_M_K {
    lea t1,  seg, sib, disp, dataSize=asz
    ldvec512 uvec1, seg, [1, t0, t1], dataSize=64
    gem5_mask_xor_epu64 zmm1, zmm2, uvec1, zmm1, opmask=opmask, size=8, ext=ZMM
};

def macroop EVEX_VPXORQ_ZMM_ZMM_P_K {
    rdip t7
    lea t1, seg, riprel, disp, dataSize=asz
    ldvec512 uvec1, seg, [1, t0, t1], dataSize=64
    gem5_mask_xor_epu64 zmm1, zmm2, uvec1, zmm1, opmask=opmask, size=8, ext=ZMM
};

'''
