microcode = '''
def macroop EVEX_VPSHUFB_XMM_XMM_XMM {
    gem5_avx_shuffle_epi8 xmm1, xmm2, xmmm, size=1, ext=XMM
};

def macroop EVEX_VPSHUFB_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_shuffle_epi8 xmm1, xmm2, uvec1, size=1, ext=XMM
};

def macroop EVEX_VPSHUFB_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_shuffle_epi8 xmm1, xmm2, uvec1, size=1, ext=XMM
};

def macroop EVEX_VPSHUFB_YMM_YMM_YMM {
    gem5_avx_shuffle_epi8 ymm1, ymm2, ymmm, size=1, ext=YMM
};

def macroop EVEX_VPSHUFB_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_shuffle_epi8 ymm1, ymm2, uvec1, size=1, ext=YMM
};

def macroop EVEX_VPSHUFB_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_shuffle_epi8 ymm1, ymm2, uvec1, size=1, ext=YMM
};

def macroop EVEX_VPSHUFB_ZMM_ZMM_ZMM {
    gem5_avx_shuffle_epi8 zmm1, zmm2, zmmm, size=1, ext=ZMM
};

def macroop EVEX_VPSHUFB_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_shuffle_epi8 zmm1, zmm2, uvec1, size=1, ext=ZMM
};

def macroop EVEX_VPSHUFB_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_shuffle_epi8 zmm1, zmm2, uvec1, size=1, ext=ZMM
};

def macroop EVEX_VPSHUFD_XMM_XMM_I {
    gem5_avx_shuffle_epu32i xmm, xmmm, imm, size=4, ext=XMM
};

def macroop EVEX_VPSHUFD_XMM_M_I {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_shuffle_epu32i xmm, uvec1, imm, size=4, ext=XMM
};

def macroop EVEX_VPSHUFD_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_shuffle_epu32i xmm, uvec1, imm, size=4, ext=XMM
};

def macroop EVEX_VPSHUFD_YMM_YMM_I {
    gem5_avx_shuffle_epu32i ymm, ymmm, imm, size=4, ext=YMM
};

def macroop EVEX_VPSHUFD_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_shuffle_epu32i ymm, uvec1, imm, size=4, ext=YMM
};

def macroop EVEX_VPSHUFD_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_shuffle_epu32i ymm, uvec1, imm, size=4, ext=YMM
};

def macroop EVEX_VPSHUFD_ZMM_ZMM_I {
    gem5_avx_shuffle_epu32i zmm, zmmm, imm, size=4, ext=ZMM
};

def macroop EVEX_VPSHUFD_ZMM_M_I {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_shuffle_epu32i zmm, uvec1, imm, size=4, ext=ZMM
};

def macroop EVEX_VPSHUFD_ZMM_P_I {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_shuffle_epu32i zmm, uvec1, imm, size=4, ext=ZMM
};

def macroop EVEX_VPSHUFHW_XMM_XMM_I {
    gem5_avx_shufflehi_epu16i xmm, xmmm, imm, size=2, ext=XMM
};

def macroop EVEX_VPSHUFHW_XMM_M_I {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_shufflehi_epu16i xmm, uvec1, imm, size=2, ext=XMM
};

def macroop EVEX_VPSHUFHW_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_shufflehi_epu16i xmm, uvec1, imm, size=2, ext=XMM
};

def macroop EVEX_VPSHUFHW_YMM_YMM_I {
    gem5_avx_shufflehi_epu16i ymm, ymmm, imm, size=2, ext=YMM
};

def macroop EVEX_VPSHUFHW_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_shufflehi_epu16i ymm, uvec1, imm, size=2, ext=YMM
};

def macroop EVEX_VPSHUFHW_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_shufflehi_epu16i ymm, uvec1, imm, size=2, ext=YMM
};

def macroop EVEX_VPSHUFHW_ZMM_ZMM_I {
    gem5_avx_shufflehi_epu16i zmm, zmmm, imm, size=2, ext=ZMM
};

def macroop EVEX_VPSHUFHW_ZMM_M_I {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_shufflehi_epu16i zmm, uvec1, imm, size=2, ext=ZMM
};

def macroop EVEX_VPSHUFHW_ZMM_P_I {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_shufflehi_epu16i zmm, uvec1, imm, size=2, ext=ZMM
};

def macroop EVEX_VPSHUFLW_XMM_XMM_I {
    gem5_avx_shufflelo_epu16i xmm, xmmm, imm, size=2, ext=XMM
};

def macroop EVEX_VPSHUFLW_XMM_M_I {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_shufflelo_epu16i xmm, uvec1, imm, size=2, ext=XMM
};

def macroop EVEX_VPSHUFLW_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_shufflelo_epu16i xmm, uvec1, imm, size=2, ext=XMM
};

def macroop EVEX_VPSHUFLW_YMM_YMM_I {
    gem5_avx_shufflelo_epu16i ymm, ymmm, imm, size=2, ext=YMM
};

def macroop EVEX_VPSHUFLW_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_shufflelo_epu16i ymm, uvec1, imm, size=2, ext=YMM
};

def macroop EVEX_VPSHUFLW_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_shufflelo_epu16i ymm, uvec1, imm, size=2, ext=YMM
};

def macroop EVEX_VPSHUFLW_ZMM_ZMM_I {
    gem5_avx_shufflelo_epu16i zmm, zmmm, imm, size=2, ext=ZMM
};

def macroop EVEX_VPSHUFLW_ZMM_M_I {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_shufflelo_epu16i zmm, uvec1, imm, size=2, ext=ZMM
};

def macroop EVEX_VPSHUFLW_ZMM_P_I {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_shufflelo_epu16i zmm, uvec1, imm, size=2, ext=ZMM
};

def macroop EVEX_VPERMD_YMM_YMM_YMM {
    gem5_avx_permutexvar_epi32 ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop EVEX_VPERMD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_permutexvar_epi32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPERMD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_permutexvar_epi32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPERMD_ZMM_ZMM_ZMM {
    gem5_avx_permutexvar_epi32 zmm1, zmm2, zmmm, size=4, ext=ZMM
};

def macroop EVEX_VPERMD_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_permutexvar_epi32 zmm1, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPERMD_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_permutexvar_epi32 zmm1, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPERMD_YMM_YMM_YMM_K {
    gem5_mask_permutexvar_epi32 ymm1, ymm2, ymmm, opmask=opmask, size=4, ext=YMM
};

def macroop EVEX_VPERMD_YMM_YMM_M_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_permutexvar_epi32 ymm1, ymm2, uvec1, opmask=opmask, size=4, ext=YMM
};

def macroop EVEX_VPERMD_YMM_YMM_P_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_permutexvar_epi32 ymm1, ymm2, uvec1, opmask=opmask, size=4, ext=YMM
};

def macroop EVEX_VPERMD_ZMM_ZMM_ZMM_K {
    gem5_mask_permutexvar_epi32 zmm1, zmm2, zmmm, opmask=opmask, size=4, ext=ZMM
};

def macroop EVEX_VPERMD_ZMM_ZMM_M_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_permutexvar_epi32 zmm1, zmm2, uvec1, opmask=opmask, size=4, ext=ZMM
};

def macroop EVEX_VPERMD_ZMM_ZMM_P_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_permutexvar_epi32 zmm1, zmm2, uvec1, opmask=opmask, size=4, ext=ZMM
};

def macroop EVEX_VPERMQ_YMM_YMM_I {
    gem5_avx_permutex_epi64i ymm1, ymmm, "(IMMEDIATE & mask(8))", size=8, ext=YMM
};

def macroop EVEX_VPERMQ_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_permutex_epi64i ymm1, uvec1, "(IMMEDIATE & mask(8))", size=8, ext=YMM
};

def macroop EVEX_VPERMQ_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_permutex_epi64i ymm1, uvec1, "(IMMEDIATE & mask(8))", size=8, ext=YMM
};

def macroop EVEX_VPERMQ_ZMM_ZMM_I {
    gem5_avx_permutex_epi64i zmm1, zmmm, "(IMMEDIATE & mask(8))", size=8, ext=ZMM
};

def macroop EVEX_VPERMQ_ZMM_M_I {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_permutex_epi64i zmm1, uvec1, "(IMMEDIATE & mask(8))", size=8, ext=ZMM
};

def macroop EVEX_VPERMQ_ZMM_P_I {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_permutex_epi64i zmm1, uvec1, "(IMMEDIATE & mask(8))", size=8, ext=ZMM
};

def macroop EVEX_VPERM2I128_YMM_YMM_YMM_I {
    gem5_avx_permute2f128_pd ymm1, ymm2, ymmm, "IMMEDIATE", size=32, ext=YMM
};

def macroop EVEX_VPERM2I128_YMM_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_permute2f128_pd ymm1, ymm2, uvec1, "IMMEDIATE", size=32, ext=YMM
};

def macroop EVEX_VPERM2I128_YMM_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_permute2f128_pd ymm1, ymm2, uvec1, "IMMEDIATE", size=32, ext=YMM
};

def macroop EVEX_VPERMI2D_XMM_XMM_XMM {
    gem5_evex_permutex2var1_epi32 xmm, xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop EVEX_VPERMI2D_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_evex_permutex2var1_epi32 xmm, xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VPERMI2D_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_evex_permutex2var1_epi32 xmm, xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VPERMI2D_YMM_YMM_YMM {
    gem5_evex_permutex2var1_epi32 ymm, ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop EVEX_VPERMI2D_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_evex_permutex2var1_epi32 ymm, ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPERMI2D_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_evex_permutex2var1_epi32 ymm, ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPERMI2D_ZMM_ZMM_ZMM {
    gem5_evex_permutex2var1_epi32 zmm, zmm1, zmm2, zmmm, size=4, ext=ZMM
};

def macroop EVEX_VPERMI2D_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_evex_permutex2var1_epi32 zmm, zmm1, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPERMI2D_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_evex_permutex2var1_epi32 zmm, zmm1, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPERMI2Q_XMM_XMM_XMM {
    gem5_evex_permutex2var1_epi64 xmm, xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop EVEX_VPERMI2Q_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_evex_permutex2var1_epi64 xmm, xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VPERMI2Q_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_evex_permutex2var1_epi64 xmm, xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VPERMI2Q_YMM_YMM_YMM {
    gem5_evex_permutex2var1_epi64 ymm, ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop EVEX_VPERMI2Q_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_evex_permutex2var1_epi64 ymm, ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VPERMI2Q_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_evex_permutex2var1_epi64 ymm, ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VPERMI2Q_ZMM_ZMM_ZMM {
    gem5_evex_permutex2var1_epi64 zmm, zmm1, zmm2, zmmm, size=8, ext=ZMM
};

def macroop EVEX_VPERMI2Q_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_evex_permutex2var1_epi64 zmm, zmm1, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VPERMI2Q_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_evex_permutex2var1_epi64 zmm, zmm1, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VPERMT2D_XMM_XMM_XMM {
    gem5_evex_permutex2var2_epi32 xmm, xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop EVEX_VPERMT2D_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_evex_permutex2var2_epi32 xmm, xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VPERMT2D_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_evex_permutex2var2_epi32 xmm, xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VPERMT2D_YMM_YMM_YMM {
    gem5_evex_permutex2var2_epi32 ymm, ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop EVEX_VPERMT2D_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_evex_permutex2var2_epi32 ymm, ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPERMT2D_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_evex_permutex2var2_epi32 ymm, ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPERMT2D_ZMM_ZMM_ZMM {
    gem5_evex_permutex2var2_epi32 zmm, zmm1, zmm2, zmmm, size=4, ext=ZMM
};

def macroop EVEX_VPERMT2D_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_evex_permutex2var2_epi32 zmm, zmm1, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPERMT2D_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_evex_permutex2var2_epi32 zmm, zmm1, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPERMT2Q_XMM_XMM_XMM {
    gem5_evex_permutex2var2_epi64 xmm, xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop EVEX_VPERMT2Q_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_evex_permutex2var2_epi64 xmm, xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VPERMT2Q_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_evex_permutex2var2_epi64 xmm, xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VPERMT2Q_YMM_YMM_YMM {
    gem5_evex_permutex2var2_epi64 ymm, ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop EVEX_VPERMT2Q_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_evex_permutex2var2_epi64 ymm, ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VPERMT2Q_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_evex_permutex2var2_epi64 ymm, ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VPERMT2Q_ZMM_ZMM_ZMM {
    gem5_evex_permutex2var2_epi64 zmm, zmm1, zmm2, zmmm, size=8, ext=ZMM
};

def macroop EVEX_VPERMT2Q_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_evex_permutex2var2_epi64 zmm, zmm1, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VPERMT2Q_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_evex_permutex2var2_epi64 zmm, zmm1, zmm2, uvec1, size=8, ext=ZMM
};

'''
