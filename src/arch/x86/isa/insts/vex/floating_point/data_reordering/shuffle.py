microcode = '''
def macroop VEX_VSHUFPS_XMM_XMM_XMM_I {
    gem5_avx_shuffle_ps xmm1, xmm2, xmmm, size=4, ext="(IMMEDIATE & mask(8)) |" + XMM
};

def macroop VEX_VSHUFPS_XMM_XMM_M_I {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_shuffle_ps xmm1, xmm2, uvec1, size=4, ext="(IMMEDIATE & mask(8)) |" + XMM
};

def macroop VEX_VSHUFPS_XMM_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_shuffle_ps xmm1, xmm2, uvec1, size=4, ext="(IMMEDIATE & mask(8)) |" + XMM
};

def macroop VEX_VSHUFPS_YMM_YMM_YMM_I {
    gem5_avx_shuffle_ps ymm1, ymm2, ymmm, size=4, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop VEX_VSHUFPS_YMM_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_shuffle_ps ymm1, ymm2, uvec1, size=4, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop VEX_VSHUFPS_YMM_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_shuffle_ps ymm1, ymm2, uvec1, size=4, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop VEX_VSHUFPD_XMM_XMM_XMM_I {
    gem5_avx_shuffle_pd xmm1, xmm2, xmmm, size=8, ext="(IMMEDIATE & mask(8)) |" + XMM
};

def macroop VEX_VSHUFPD_XMM_XMM_M_I {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_shuffle_pd xmm1, xmm2, uvec1, size=8, ext="(IMMEDIATE & mask(8)) |" + XMM
};

def macroop VEX_VSHUFPD_XMM_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_shuffle_pd xmm1, xmm2, uvec1, size=8, ext="(IMMEDIATE & mask(8)) |" + XMM
};

def macroop VEX_VSHUFPD_YMM_YMM_YMM_I {
    gem5_avx_shuffle_pd ymm1, ymm2, ymmm, size=8, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop VEX_VSHUFPD_YMM_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_shuffle_pd ymm1, ymm2, uvec1, size=8, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop VEX_VSHUFPD_YMM_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_shuffle_pd ymm1, ymm2, uvec1, size=8, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop VEX_VPERMD_XMM_XMM_XMM {
    gem5_avx_permutexvar_epi32 xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop VEX_VPERMD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_permutexvar_epi32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VPERMD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_permutexvar_epi32 xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VPERMD_YMM_YMM_YMM {
    gem5_avx_permutexvar_epi32 ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop VEX_VPERMD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_permutexvar_epi32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VPERMD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_permutexvar_epi32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VPERMILPD_XMM_XMM_XMM {
    gem5_avx_permutevar_pd xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop VEX_VPERMILPD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_permutevar_pd xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VPERMILPD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_permutevar_pd xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VPERMILPD_YMM_YMM_YMM {
    gem5_avx_permutevar_pd ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop VEX_VPERMILPD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_permutevar_pd ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop VEX_VPERMILPD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_permutevar_pd ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop VEX_VPERMILPD_XMM_XMM_I {
    gem5_avx_permute_pd xmm1, xmmm, size=8, ext="(IMMEDIATE & mask(8)) |" + XMM
};

def macroop VEX_VPERMILPD_XMM_M_I {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_permute_pd xmm1, uvec1, size=8, ext="(IMMEDIATE & mask(8)) |" + XMM
};

def macroop VEX_VPERMILPD_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_permute_pd xmm1, uvec1, size=8, ext="(IMMEDIATE & mask(8)) |" + XMM
};

def macroop VEX_VPERMILPD_YMM_YMM_I {
    gem5_avx_permute_pd ymm1, ymmm, size=8, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop VEX_VPERMILPD_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_permute_pd ymm1, uvec1, size=8, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop VEX_VPERMILPD_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_permute_pd ymm1, uvec1, size=8, ext="(IMMEDIATE & mask(8)) |" + YMM
};

def macroop VEX_VPERMPS_YMM_YMM_YMM {
    gem5_avx_permutexvar_epi32 ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop VEX_VPERMPS_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_permutexvar_epi32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VPERMPS_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_permutexvar_epi32 ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VPERMPD_YMM_YMM_I {
    gem5_avx_permutex_epi64i ymm1, ymmm, "IMMEDIATE", size=8, ext=YMM
};

def macroop VEX_VPERMPD_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_permutex_epi64i ymm1, uvec1, "IMMEDIATE", size=8, ext=YMM
};

def macroop VEX_VPERMPD_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_permutex_epi64i ymm1, uvec1, "IMMEDIATE", size=8, ext=YMM
};

def macroop VEX_VPERM2F128_YMM_YMM_YMM_I {
    gem5_avx_permute2f128_pd ymm1, ymm2, ymmm, "IMMEDIATE", size=32, ext=YMM
};

def macroop VEX_VPERM2F128_YMM_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_permute2f128_pd ymm1, ymm2, uvec1, "IMMEDIATE", size=32, ext=YMM
};

def macroop VEX_VPERM2F128_YMM_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_permute2f128_pd ymm1, ymm2, uvec1, "IMMEDIATE", size=32, ext=YMM
};

'''
