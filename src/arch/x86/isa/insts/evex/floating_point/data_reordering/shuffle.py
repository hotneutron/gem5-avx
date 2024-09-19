microcode = '''
def macroop EVEX_VSHUFPS_XMM_XMM_XMM_I {
    gem5_avx_shuffle_ps xmm1, xmm2, xmmm, size=4, ext="(IMMEDIATE & mask(8)) |" + XMM
};

def macroop EVEX_VSHUFPS_XMM_XMM_M_I {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_shuffle_ps xmm1, xmm2, uvec1, size=4, ext="(IMMEDIATE & mask(8)) |" + XMM
};

def macroop EVEX_VSHUFPS_XMM_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_shuffle_ps xmm1, xmm2, uvec1, size=4, ext="(IMMEDIATE & mask(8)) |" + XMM
};

def macroop EVEX_VSHUFPS_YMM_YMM_YMM_I {
    gem5_avx_shuffle_ps ymm1, ymm2, ymmm, size=4, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop EVEX_VSHUFPS_YMM_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_shuffle_ps ymm1, ymm2, uvec1, size=4, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop EVEX_VSHUFPS_YMM_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_shuffle_ps ymm1, ymm2, uvec1, size=4, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop EVEX_VSHUFPS_ZMM_ZMM_ZMM_I {
    gem5_avx_shuffle_ps zmm1, zmm2, zmmm, size=4, ext="(IMMEDIATE & mask(8)) |" + ZMM
};

def macroop EVEX_VSHUFPS_ZMM_ZMM_M_I {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_shuffle_ps zmm1, zmm2, uvec1, size=4, ext="(IMMEDIATE & mask(8)) |" + ZMM
};

def macroop EVEX_VSHUFPS_ZMM_ZMM_P_I {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_shuffle_ps zmm1, zmm2, uvec1, size=4, ext="(IMMEDIATE & mask(8)) |" + ZMM
};

def macroop EVEX_VSHUFPD_XMM_XMM_XMM_I {
    gem5_avx_shuffle_pd xmm1, xmm2, xmmm, size=8, ext="(IMMEDIATE & mask(8)) |" + XMM
};

def macroop EVEX_VSHUFPD_XMM_XMM_M_I {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_shuffle_pd xmm1, xmm2, uvec1, size=8, ext="(IMMEDIATE & mask(8)) |" + XMM
};

def macroop EVEX_VSHUFPD_XMM_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_shuffle_pd xmm1, xmm2, uvec1, size=8, ext="(IMMEDIATE & mask(8)) |" + XMM
};

def macroop EVEX_VSHUFPD_YMM_YMM_YMM_I {
    gem5_avx_shuffle_pd ymm1, ymm2, ymmm, size=8, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop EVEX_VSHUFPD_YMM_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_shuffle_pd ymm1, ymm2, uvec1, size=8, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop EVEX_VSHUFPD_YMM_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_shuffle_pd ymm1, ymm2, uvec1, size=8, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop EVEX_VSHUFPD_ZMM_ZMM_ZMM_I {
    gem5_avx_shuffle_pd zmm1, zmm2, zmmm, size=8, ext="(IMMEDIATE & mask(8)) |" + ZMM
};

def macroop EVEX_VSHUFPD_ZMM_ZMM_M_I {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_shuffle_pd zmm1, zmm2, uvec1, size=8, ext="(IMMEDIATE & mask(8)) |" + ZMM
};

def macroop EVEX_VSHUFPD_ZMM_ZMM_P_I {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_shuffle_pd zmm1, zmm2, uvec1, size=8, ext="(IMMEDIATE & mask(8)) |" + ZMM
};

def macroop EVEX_VSHUFF32X4_YMM_YMM_YMM_I {
    gem5_evex_shuffle_32x4 ymm1, ymm2, ymmm, size=4, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop EVEX_VSHUFF32X4_YMM_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_evex_shuffle_32x4 ymm1, ymm2, uvec1, size=4, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop EVEX_VSHUFF32X4_YMM_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_evex_shuffle_32x4 ymm1, ymm2, uvec1, size=4, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop EVEX_VSHUFF32X4_ZMM_ZMM_ZMM_I {
    gem5_evex_shuffle_32x4 zmm1, zmm2, zmmm, size=4, ext="(IMMEDIATE & mask(8)) |" + ZMM
};

def macroop EVEX_VSHUFF32X4_ZMM_ZMM_M_I {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_evex_shuffle_32x4 zmm1, zmm2, uvec1, size=4, ext="(IMMEDIATE & mask(8)) |" + ZMM
};

def macroop EVEX_VSHUFF32X4_ZMM_ZMM_P_I {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_evex_shuffle_32x4 zmm1, zmm2, uvec1, size=4, ext="(IMMEDIATE & mask(8)) |" + ZMM
};

def macroop EVEX_VSHUFF64X2_YMM_YMM_YMM_I {
    gem5_evex_shuffle_64x2 ymm1, ymm2, ymmm, size=8, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop EVEX_VSHUFF64X2_YMM_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_evex_shuffle_64x2 ymm1, ymm2, uvec1, size=8, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop EVEX_VSHUFF64X2_YMM_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_evex_shuffle_64x2 ymm1, ymm2, uvec1, size=8, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop EVEX_VSHUFF64X2_ZMM_ZMM_ZMM_I {
    gem5_evex_shuffle_64x2 zmm1, zmm2, zmmm, size=8, ext="(IMMEDIATE & mask(8)) |" + ZMM
};

def macroop EVEX_VSHUFF64X2_ZMM_ZMM_M_I {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_evex_shuffle_64x2 zmm1, zmm2, uvec1, size=8, ext="(IMMEDIATE & mask(8)) |" + ZMM
};

def macroop EVEX_VSHUFF64X2_ZMM_ZMM_P_I {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_evex_shuffle_64x2 zmm1, zmm2, uvec1, size=8, ext="(IMMEDIATE & mask(8)) |" + ZMM
};

def macroop EVEX_VPERMILPD_XMM_XMM_XMM {
    gem5_avx_permutevar_pd xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop EVEX_VPERMILPD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_permutevar_pd xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VPERMILPD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_permutevar_pd xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VPERMILPD_XMM_XMM_I {
    gem5_avx_permute_pd xmm1, xmmm, size=8, ext="(IMMEDIATE & mask(8)) |" + XMM
};

def macroop EVEX_VPERMILPD_XMM_M_I {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_permute_pd xmm1, uvec1, size=8, ext="(IMMEDIATE & mask(8)) |" + XMM
};

def macroop EVEX_VPERMILPD_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_permute_pd xmm1, uvec1, size=8, ext="(IMMEDIATE & mask(8)) |" + XMM
};

def macroop EVEX_VPERMILPD_YMM_YMM_YMM {
    gem5_avx_permutevar_pd ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop EVEX_VPERMILPD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_permutevar_pd ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VPERMILPD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_permutevar_pd ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VPERMILPD_YMM_YMM_I {
    gem5_avx_permute_pd ymm1, ymmm, size=8, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop EVEX_VPERMILPD_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_permute_pd ymm1, uvec1, size=8, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop EVEX_VPERMILPD_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_permute_pd ymm1, uvec1, size=8, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop EVEX_VPERMILPD_ZMM_ZMM_ZMM {
    gem5_avx_permutevar_pd zmm1, zmm2, zmmm, size=8, ext=ZMM
};

def macroop EVEX_VPERMILPD_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_permutevar_pd zmm1, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VPERMILPD_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_permutevar_pd zmm1, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VPERMILPD_ZMM_ZMM_I {
    gem5_avx_permute_pd zmm1, zmmm, size=8, ext="(IMMEDIATE & mask(8)) |" + ZMM
};

def macroop EVEX_VPERMILPD_ZMM_M_I {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_permute_pd zmm1, uvec1, size=8, ext="(IMMEDIATE & mask(8)) |" + ZMM
};

def macroop EVEX_VPERMILPD_ZMM_P_I {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_permute_pd zmm1, uvec1, size=8, ext="(IMMEDIATE & mask(8)) |" + ZMM
};

def macroop EVEX_VPERMPS_YMM_YMM_YMM {
    gem5_avx_permutexvar_epi32 ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop EVEX_VPERMPS_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_permutexvar_epi32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPERMPS_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_permutexvar_epi32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPERMPS_ZMM_ZMM_ZMM {
    gem5_avx_permutexvar_epi32 zmm1, zmm2, zmmm, size=4, ext=ZMM
};

def macroop EVEX_VPERMPS_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_permutexvar_epi32 zmm1, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPERMPS_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_permutexvar_epi32 zmm1, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPERMPD_YMM_YMM_YMM {
    gem5_avx_permutexvar_epi64 ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop EVEX_VPERMPD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_permutexvar_epi64 ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VPERMPD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_permutexvar_epi64 ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VPERMPD_ZMM_ZMM_ZMM {
    gem5_avx_permutexvar_epi64 zmm1, zmm2, zmmm, size=8, ext=ZMM
};

def macroop EVEX_VPERMPD_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_permutexvar_epi64 zmm1, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VPERMPD_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_permutexvar_epi64 zmm1, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VPERMPD_YMM_YMM_I {
    gem5_avx_permutex_epi64i ymm1, ymmm, "(IMMEDIATE & mask(8))", size=8, ext=YMM
};

def macroop EVEX_VPERMPD_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_permutex_epi64i ymm1, uvec1, "(IMMEDIATE & mask(8))", size=8, ext=YMM
};

def macroop EVEX_VPERMPD_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_permutex_epi64i ymm1, uvec1, "(IMMEDIATE & mask(8))", size=8, ext=YMM
};

def macroop EVEX_VPERMPD_ZMM_ZMM_I {
    gem5_avx_permutex_epi64i zmm1, zmmm, "(IMMEDIATE & mask(8))", size=8, ext=ZMM
};

def macroop EVEX_VPERMPD_ZMM_M_I {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_permutex_epi64i zmm1, uvec1, "(IMMEDIATE & mask(8))", size=8, ext=ZMM
};

def macroop EVEX_VPERMPD_ZMM_P_I {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_permutex_epi64i zmm1, uvec1, "(IMMEDIATE & mask(8))", size=8, ext=ZMM
};

def macroop EVEX_VPERM2F128_YMM_YMM_YMM_I {
    gem5_avx_permute2f128_pd ymm1, ymm2, ymmm, "(IMMEDIATE & mask(8))", size=32, ext=YMM
};

def macroop EVEX_VPERM2F128_YMM_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_permute2f128_pd ymm1, ymm2, uvec1, "(IMMEDIATE & mask(8))", size=32, ext=YMM
};

def macroop EVEX_VPERM2F128_YMM_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_permute2f128_pd ymm1, ymm2, uvec1, "(IMMEDIATE & mask(8))", size=32, ext=YMM
};

def macroop EVEX_VPERMI2PS_XMM_XMM_XMM {
    gem5_evex_permutex2var1_epi32 xmm, xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop EVEX_VPERMI2PS_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_evex_permutex2var1_epi32 xmm, xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VPERMI2PS_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_evex_permutex2var1_epi32 xmm, xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VPERMI2PS_YMM_YMM_YMM {
    gem5_evex_permutex2var1_epi32 ymm, ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop EVEX_VPERMI2PS_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_evex_permutex2var1_epi32 ymm, ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPERMI2PS_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_evex_permutex2var1_epi32 ymm, ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPERMI2PS_ZMM_ZMM_ZMM {
    gem5_evex_permutex2var1_epi32 zmm, zmm1, zmm2, zmmm, size=4, ext=ZMM
};

def macroop EVEX_VPERMI2PS_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_evex_permutex2var1_epi32 zmm, zmm1, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPERMI2PS_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_evex_permutex2var1_epi32 zmm, zmm1, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPERMI2PD_XMM_XMM_XMM {
    gem5_evex_permutex2var1_epi64 xmm, xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop EVEX_VPERMI2PD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_evex_permutex2var1_epi64 xmm, xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VPERMI2PD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_evex_permutex2var1_epi64 xmm, xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VPERMI2PD_YMM_YMM_YMM {
    gem5_evex_permutex2var1_epi64 ymm, ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop EVEX_VPERMI2PD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_evex_permutex2var1_epi64 ymm, ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VPERMI2PD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_evex_permutex2var1_epi64 ymm, ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VPERMI2PD_ZMM_ZMM_ZMM {
    gem5_evex_permutex2var1_epi64 zmm, zmm1, zmm2, zmmm, size=8, ext=ZMM
};

def macroop EVEX_VPERMI2PD_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_evex_permutex2var1_epi64 zmm, zmm1, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VPERMI2PD_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_evex_permutex2var1_epi64 zmm, zmm1, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VPERMT2PS_XMM_XMM_XMM {
    gem5_evex_permutex2var2_epi32 xmm, xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop EVEX_VPERMT2PS_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_evex_permutex2var2_epi32 xmm, xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VPERMT2PS_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_evex_permutex2var2_epi32 xmm, xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VPERMT2PS_YMM_YMM_YMM {
    gem5_evex_permutex2var2_epi32 ymm, ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop EVEX_VPERMT2PS_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_evex_permutex2var2_epi32 ymm, ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPERMT2PS_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_evex_permutex2var2_epi32 ymm, ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VPERMT2PS_ZMM_ZMM_ZMM {
    gem5_evex_permutex2var2_epi32 zmm, zmm1, zmm2, zmmm, size=4, ext=ZMM
};

def macroop EVEX_VPERMT2PS_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_evex_permutex2var2_epi32 zmm, zmm1, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPERMT2PS_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_evex_permutex2var2_epi32 zmm, zmm1, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VPERMT2PD_XMM_XMM_XMM {
    gem5_evex_permutex2var2_epi64 xmm, xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop EVEX_VPERMT2PD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_evex_permutex2var2_epi64 xmm, xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VPERMT2PD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_evex_permutex2var2_epi64 xmm, xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VPERMT2PD_YMM_YMM_YMM {
    gem5_evex_permutex2var2_epi64 ymm, ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop EVEX_VPERMT2PD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_evex_permutex2var2_epi64 ymm, ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VPERMT2PD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_evex_permutex2var2_epi64 ymm, ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VPERMT2PD_ZMM_ZMM_ZMM {
    gem5_evex_permutex2var2_epi64 zmm, zmm1, zmm2, zmmm, size=8, ext=ZMM
};

def macroop EVEX_VPERMT2PD_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_evex_permutex2var2_epi64 zmm, zmm1, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VPERMT2PD_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_evex_permutex2var2_epi64 zmm, zmm1, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VPERMPS_YMM_YMM_YMM_K {
    gem5_mask_permutexvar_epi32 ymm1, ymm2, ymmm, ymm1, opmask=opmask, size=4, ext=YMM
};

def macroop EVEX_VPERMPS_YMM_YMM_M_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_permutexvar_epi32 ymm1, ymm2, uvec1, ymm1, opmask=opmask, size=4, ext=YMM
};

def macroop EVEX_VPERMPS_YMM_YMM_P_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_permutexvar_epi32 ymm1, ymm2, uvec1, ymm1, opmask=opmask, size=4, ext=YMM
};

def macroop EVEX_VPERMPS_ZMM_ZMM_ZMM_K {
    gem5_mask_permutexvar_epi32 zmm1, zmm2, zmmm, zmm1, opmask=opmask, size=4, ext=ZMM
};

def macroop EVEX_VPERMPS_ZMM_ZMM_M_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_permutexvar_epi32 zmm1, zmm2, uvec1, zmm1, opmask=opmask, size=4, ext=ZMM
};

def macroop EVEX_VPERMPS_ZMM_ZMM_P_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_permutexvar_epi32 zmm1, zmm2, uvec1, zmm1, opmask=opmask, size=4, ext=ZMM
};

def macroop EVEX_VPERMPD_YMM_YMM_YMM_K {
    gem5_mask_permutexvar_epi64 ymm1, ymm2, ymmm, ymm1, opmask=opmask, size=8, ext=YMM
};

def macroop EVEX_VPERMPD_YMM_YMM_M_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_permutexvar_epi64 ymm1, ymm2, uvec1, ymm1, opmask=opmask, size=8, ext=YMM
};

def macroop EVEX_VPERMPD_YMM_YMM_P_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_permutexvar_epi64 ymm1, ymm2, uvec1, ymm1, opmask=opmask, size=8, ext=YMM
};

def macroop EVEX_VPERMPD_ZMM_ZMM_ZMM_K {
    gem5_mask_permutexvar_epi64 zmm1, zmm2, zmmm, zmm1, opmask=opmask, size=8, ext=ZMM
};

def macroop EVEX_VPERMPD_ZMM_ZMM_M_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_permutexvar_epi64 zmm1, zmm2, uvec1, zmm1, opmask=opmask, size=8, ext=ZMM
};

def macroop EVEX_VPERMPD_ZMM_ZMM_P_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_permutexvar_epi64 zmm1, zmm2, uvec1, zmm1, opmask=opmask, size=8, ext=ZMM
};

'''
