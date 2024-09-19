microcode = '''
def macroop VEX_VPSHUFB_XMM_XMM_XMM {
    gem5_avx_shuffle_epi8 xmm1, xmm2, xmmm, size=1, ext=XMM
};

def macroop VEX_VPSHUFB_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_shuffle_epi8 xmm1, xmm2, uvec1, size=1, ext=XMM
};

def macroop VEX_VPSHUFB_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_shuffle_epi8 xmm1, xmm2, uvec1, size=1, ext=XMM
};

def macroop VEX_VPSHUFB_YMM_YMM_YMM {
    gem5_avx_shuffle_epi8 ymm1, ymm2, ymmm, size=1, ext=YMM
};

def macroop VEX_VPSHUFB_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_shuffle_epi8 ymm1, ymm2, uvec1, size=1, ext=YMM
};

def macroop VEX_VPSHUFB_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_shuffle_epi8 ymm1, ymm2, uvec1, size=1, ext=YMM
};

def macroop VEX_VPSHUFD_XMM_XMM_I {
    gem5_avx_shuffle_epu32i xmm, xmmm, imm, size=4, ext=XMM
};

def macroop VEX_VPSHUFD_XMM_M_I {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_shuffle_epu32i xmm, uvec1, imm, size=4, ext=XMM
};

def macroop VEX_VPSHUFD_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_shuffle_epu32i xmm, uvec1, imm, size=4, ext=XMM
};

def macroop VEX_VPSHUFD_YMM_YMM_I {
    gem5_avx_shuffle_epu32i ymm, ymmm, imm, size=4, ext=YMM
};

def macroop VEX_VPSHUFD_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_shuffle_epu32i ymm, uvec1, imm, size=4, ext=YMM
};

def macroop VEX_VPSHUFD_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_shuffle_epu32i ymm, uvec1, imm, size=4, ext=YMM
};

def macroop VEX_VPSHUFHW_XMM_XMM_I {
    gem5_avx_shufflehi_epu16i xmm, xmmm, imm, size=2, ext=XMM
};

def macroop VEX_VPSHUFHW_XMM_M_I {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_shufflehi_epu16i xmm, uvec1, imm, size=2, ext=XMM
};

def macroop VEX_VPSHUFHW_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_shufflehi_epu16i xmm, uvec1, imm, size=2, ext=XMM
};

def macroop VEX_VPSHUFHW_YMM_YMM_I {
    gem5_avx_shufflehi_epu16i ymm, ymmm, imm, size=2, ext=YMM
};

def macroop VEX_VPSHUFHW_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_shufflehi_epu16i ymm, uvec1, imm, size=2, ext=YMM
};

def macroop VEX_VPSHUFHW_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_shufflehi_epu16i ymm, uvec1, imm, size=2, ext=YMM
};

def macroop VEX_VPSHUFLW_XMM_XMM_I {
    gem5_avx_shufflelo_epu16i xmm, xmmm, imm, size=2, ext=XMM
};

def macroop VEX_VPSHUFLW_XMM_M_I {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_shufflelo_epu16i xmm, uvec1, imm, size=2, ext=XMM
};

def macroop VEX_VPSHUFLW_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_shufflelo_epu16i xmm, uvec1, imm, size=2, ext=XMM
};

def macroop VEX_VPSHUFLW_YMM_YMM_I {
    gem5_avx_shufflelo_epu16i ymm, ymmm, imm, size=2, ext=YMM
};

def macroop VEX_VPSHUFLW_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_shufflelo_epu16i ymm, uvec1, imm, size=2, ext=YMM
};

def macroop VEX_VPSHUFLW_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_shufflelo_epu16i ymm, uvec1, imm, size=2, ext=YMM
};

def macroop VEX_VPERMQ_YMM_YMM_I {
    gem5_avx_permutex_epi64i ymm1, ymmm, "IMMEDIATE", size=8, ext=YMM
};

def macroop VEX_VPERMQ_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_permutex_epi64i ymm1, uvec1, "IMMEDIATE", size=8, ext=YMM
};

def macroop VEX_VPERMQ_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_permutex_epi64i ymm1, uvec1, "IMMEDIATE", size=8, ext=YMM
};

def macroop VEX_VPERM2I128_YMM_YMM_YMM_I {
    gem5_avx_permute2f128_pd ymm1, ymm2, ymmm, "IMMEDIATE", size=32, ext=YMM
};

def macroop VEX_VPERM2I128_YMM_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_permute2f128_pd ymm1, ymm2, uvec1, "IMMEDIATE", size=32, ext=YMM
};

def macroop VEX_VPERM2I128_YMM_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_permute2f128_pd ymm1, ymm2, uvec1, "IMMEDIATE", size=32, ext=YMM
};

def macroop VEX_KSHIFTRB_K_K_I {
    gem5_avx_kshiftr k, km, size=1, ext="IMMEDIATE"
};

def macroop VEX_KSHIFTRW_K_K_I {
    gem5_avx_kshiftr k, km, size=2, ext="IMMEDIATE"
};

def macroop VEX_KSHIFTRD_K_K_I {
    gem5_avx_kshiftr k, km, size=4, ext="IMMEDIATE"
};

def macroop VEX_KSHIFTRQ_K_K_I {
    gem5_avx_kshiftr k, km, size=8, ext="IMMEDIATE"
};

def macroop VEX_KSHIFTLB_K_K_I {
    gem5_avx_kshiftl k, km, size=1, ext="IMMEDIATE"
};

def macroop VEX_KSHIFTLW_K_K_I {
    gem5_avx_kshiftl k, km, size=2, ext="IMMEDIATE"
};

def macroop VEX_KSHIFTLD_K_K_I {
    gem5_avx_kshiftl k, km, size=4, ext="IMMEDIATE"
};

def macroop VEX_KSHIFTLQ_K_K_I {
    gem5_avx_kshiftl k, km, size=8, ext="IMMEDIATE"
};

'''
