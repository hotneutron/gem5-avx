microcode = '''
def macroop EVEX_VPMULLD_XMM_XMM_XMM {
    gem5_avx_mullo_epi32 xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop EVEX_VPMULLD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_mullo_epi32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VPMULLD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_mullo_epi32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VPMULLD_YMM_YMM_YMM {
    gem5_avx_mullo_epi32 ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop EVEX_VPMULLD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_mullo_epi32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPMULLD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_mullo_epi32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPMULLD_ZMM_ZMM_ZMM {
    gem5_avx_mullo_epi32 zmm1, zmm2, zmmm, size=4, ext=ZMM
};

def macroop EVEX_VPMULLD_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_mullo_epi32 zmm1, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPMULLD_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_mullo_epi32 zmm1, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPMULLQ_XMM_XMM_XMM {
    gem5_avx_mullo_epi64 xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop EVEX_VPMULLQ_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_mullo_epi64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VPMULLQ_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_mullo_epi64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VPMULLQ_YMM_YMM_YMM {
    gem5_avx_mullo_epi64 ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop EVEX_VPMULLQ_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_mullo_epi64 ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VPMULLQ_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_mullo_epi64 ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VPMULLQ_ZMM_ZMM_ZMM {
    gem5_avx_mullo_epi64 zmm1, zmm2, zmmm, size=8, ext=ZMM
};

def macroop EVEX_VPMULLQ_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_mullo_epi64 zmm1, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VPMULLQ_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_mullo_epi64 zmm1, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VPMULLD_XMM_XMM_XMM_K {
    gem5_mask_mullo_epi32 xmm1, xmm2, xmmm, opmask=opmask, size=4, ext=XMM
};

def macroop EVEX_VPMULLD_XMM_XMM_M_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_mullo_epi32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VPMULLD_XMM_XMM_P_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_mullo_epi32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VPMULLD_YMM_YMM_YMM_K {
    gem5_mask_mullo_epi32 ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop EVEX_VPMULLD_YMM_YMM_M_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_mullo_epi32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPMULLD_YMM_YMM_P_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_mullo_epi32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPMULLD_ZMM_ZMM_K {
    gem5_mask_mullo_epi32 zmm1, zmm2, zmmm, size=4, ext=ZMM
};

def macroop EVEX_VPMULLD_ZMM_M_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_mullo_epi32 zmm1, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPMULLD_ZMM_P_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_mullo_epi32 zmm1, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPMULUDQ_XMM_XMM_XMM {
    gem5_avx_mul_epu64 xmm1, xmm2, xmmm, srcSize=4, destSize=8, ext=XMM
};

def macroop EVEX_VPMULUDQ_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_mul_epu64 xmm1, xmm2, uvec1, srcSize=4, destSize=8, ext=XMM
};

def macroop EVEX_VPMULUDQ_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_mul_epu64 xmm1, xmm2, uvec1, srcSize=4, destSize=8, ext=XMM
};

def macroop EVEX_VPMULUDQ_YMM_YMM_YMM {
    gem5_avx_mul_epu64 ymm1, ymm2, ymmm, srcSize=4, destSize=8, ext=YMM
};

def macroop EVEX_VPMULUDQ_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_mul_epu64 ymm1, ymm2, uvec1, srcSize=4, destSize=8, ext=YMM
};

def macroop EVEX_VPMULUDQ_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_mul_epu64 ymm1, ymm2, uvec1, srcSize=4, destSize=8, ext=YMM
};

def macroop EVEX_VPMULUDQ_ZMM_ZMM_ZMM {
    gem5_avx_mul_epu64 zmm1, zmm2, zmmm, srcSize=4, destSize=8, ext=ZMM
};

def macroop EVEX_VPMULUDQ_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_mul_epu64 zmm1, zmm2, uvec1, srcSize=4, destSize=8, ext=ZMM
};

def macroop EVEX_VPMULUDQ_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_mul_epu64 zmm1, zmm2, uvec1, srcSize=4, destSize=8, ext=ZMM
};

def macroop EVEX_VPMULDQ_XMM_XMM_XMM {
    gem5_avx_mul_epi64 xmm1, xmm2, xmmm, srcSize=4, destSize=8, ext=XMM
};

def macroop EVEX_VPMULDQ_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_mul_epi64 xmm1, xmm2, uvec1, srcSize=4, destSize=8, ext=XMM
};

def macroop EVEX_VPMULDQ_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_mul_epi64 xmm1, xmm2, uvec1, srcSize=4, destSize=8, ext=XMM
};

def macroop EVEX_VPMULDQ_YMM_YMM_YMM {
    gem5_avx_mul_epi64 ymm1, ymm2, ymmm, srcSize=4, destSize=8, ext=YMM
};

def macroop EVEX_VPMULDQ_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_mul_epi64 ymm1, ymm2, uvec1, srcSize=4, destSize=8, ext=YMM
};

def macroop EVEX_VPMULDQ_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_mul_epi64 ymm1, ymm2, uvec1, srcSize=4, destSize=8, ext=YMM
};

def macroop EVEX_VPMULDQ_ZMM_ZMM_ZMM {
    gem5_avx_mul_epi64 zmm1, zmm2, zmmm, srcSize=4, destSize=8, ext=ZMM
};

def macroop EVEX_VPMULDQ_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_mul_epi64 zmm1, zmm2, uvec1, srcSize=4, destSize=8, ext=ZMM
};

def macroop EVEX_VPMULDQ_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_mul_epi64 zmm1, zmm2, uvec1, srcSize=4, destSize=8, ext=ZMM
};

'''
