microcode = '''
def macroop EVEX_VPCONFLICTD_XMM_XMM {
    gem5_avx_conflict_epi32 xmm, xmmm, size=4, ext=XMM
};

def macroop EVEX_VPCONFLICTD_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_conflict_epi32 xmm, uvec1, size=4, ext=XMM
};

def macroop EVEX_VPCONFLICTD_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_conflict_epi32 xmm, uvec1, size=4, ext=XMM
};

def macroop EVEX_VPCONFLICTD_YMM_YMM {
    gem5_avx_conflict_epi32 ymm, ymmm, size=4, ext=YMM
};

def macroop EVEX_VPCONFLICTD_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_conflict_epi32 ymm, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPCONFLICTD_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_conflict_epi32 ymm, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPCONFLICTD_ZMM_ZMM {
    gem5_avx_conflict_epi32 zmm, zmmm, size=4, ext=ZMM
};

def macroop EVEX_VPCONFLICTD_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_conflict_epi32 zmm, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPCONFLICTD_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_conflict_epi32 zmm, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPCONFLICTQ_XMM_XMM {
    gem5_avx_conflict_epi64 xmm, xmmm, size=8, ext=XMM
};

def macroop EVEX_VPCONFLICTQ_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_conflict_epi64 xmm, uvec1, size=8, ext=XMM
};

def macroop EVEX_VPCONFLICTQ_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_conflict_epi64 xmm, uvec1, size=8, ext=XMM
};

def macroop EVEX_VPCONFLICTQ_YMM_YMM {
    gem5_avx_conflict_epi64 ymm, ymmm, size=8, ext=YMM
};

def macroop EVEX_VPCONFLICTQ_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_conflict_epi64 ymm, uvec1, size=8, ext=YMM
};

def macroop EVEX_VPCONFLICTQ_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_conflict_epi64 ymm, uvec1, size=8, ext=YMM
};

def macroop EVEX_VPCONFLICTQ_ZMM_ZMM {
    gem5_avx_conflict_epi64 zmm, zmmm, size=8, ext=ZMM
};

def macroop EVEX_VPCONFLICTQ_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_conflict_epi64 zmm, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VPCONFLICTQ_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_conflict_epi64 zmm, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VPCONFLICTD_XMM_XMM_K {
    gem5_mask_conflict_epi32 xmm, xmmm, opmask=opmask, src2=xmm, size=4, ext=XMM
};

def macroop EVEX_VPCONFLICTD_XMM_M_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_conflict_epi32 xmm, uvec1, opmask=opmask, src2=xmm, size=4, ext=XMM
};

def macroop EVEX_VPCONFLICTD_XMM_P_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_conflict_epi32 xmm, uvec1, opmask=opmask, src2=xmm, size=4, ext=XMM
};

def macroop EVEX_VPCONFLICTD_YMM_YMM_K {
    gem5_mask_conflict_epi32 ymm, ymmm, opmask=opmask, src2=ymm, size=4, ext=YMM
};

def macroop EVEX_VPCONFLICTD_YMM_M_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_conflict_epi32 ymm, uvec1, opmask=opmask, src2=ymm, size=4, ext=YMM
};

def macroop EVEX_VPCONFLICTD_YMM_P_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_conflict_epi32 ymm, uvec1, opmask=opmask, src2=ymm, size=4, ext=YMM
};

def macroop EVEX_VPCONFLICTD_ZMM_ZMM_K {
    gem5_mask_conflict_epi32 zmm, zmmm, opmask=opmask, src2=zmm, size=4, ext=ZMM
};

def macroop EVEX_VPCONFLICTD_ZMM_M_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_conflict_epi32 zmm, uvec1, opmask=opmask, src2=zmm, size=4, ext=ZMM
};

def macroop EVEX_VPCONFLICTD_ZMM_P_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_conflict_epi32 zmm, uvec1, opmask=opmask, src2=zmm, size=4, ext=ZMM
};

def macroop EVEX_VPCONFLICTQ_XMM_XMM_K {
    gem5_mask_conflict_epi64 xmm, xmmm, opmask=opmask, src2=xmm, size=8, ext=XMM
};

def macroop EVEX_VPCONFLICTQ_XMM_M_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_conflict_epi64 xmm, uvec1, opmask=opmask, src2=xmm, size=8, ext=XMM
};

def macroop EVEX_VPCONFLICTQ_XMM_P_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_conflict_epi64 xmm, uvec1, opmask=opmask, src2=xmm, size=8, ext=XMM
};

def macroop EVEX_VPCONFLICTQ_YMM_YMM_K {
    gem5_mask_conflict_epi64 ymm, ymmm, opmask=opmask, src2=ymm, size=8, ext=YMM
};

def macroop EVEX_VPCONFLICTQ_YMM_M_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_conflict_epi64 ymm, uvec1, opmask=opmask, src2=ymm, size=8, ext=YMM
};

def macroop EVEX_VPCONFLICTQ_YMM_P_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_conflict_epi64 ymm, uvec1, opmask=opmask, src2=ymm, size=8, ext=YMM
};

def macroop EVEX_VPCONFLICTQ_ZMM_ZMM_K {
    gem5_mask_conflict_epi64 zmm, zmmm, opmask=opmask, src2=zmm, size=8, ext=ZMM
};

def macroop EVEX_VPCONFLICTQ_ZMM_M_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_conflict_epi64 zmm, uvec1, opmask=opmask, src2=zmm, size=8, ext=ZMM
};

def macroop EVEX_VPCONFLICTQ_ZMM_P_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_conflict_epi64 zmm, uvec1, opmask=opmask, src2=zmm, size=8, ext=ZMM
};

'''
