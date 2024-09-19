microcode = '''
def macroop VEX_VCMPPS_XMM_XMM_XMM_I {
    gem5_avx_cmp_ps xmm1, xmm2, xmmm, size=4, ext="(IMMEDIATE & mask(5)) |" + XMM
};

def macroop VEX_VCMPPS_XMM_XMM_M_I {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_cmp_ps xmm1, xmm2, uvec1, size=4, ext="(IMMEDIATE & mask(5)) |" + XMM
};

def macroop VEX_VCMPPS_XMM_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_cmp_ps xmm1, xmm2, uvec1, size=4, ext="(IMMEDIATE & mask(5)) |" + XMM
};

def macroop VEX_VCMPPS_YMM_YMM_YMM_I {
    gem5_avx_cmp_ps ymm1, ymm2, ymmm, size=4, ext="(IMMEDIATE & mask(5)) |" + YMM
};

def macroop VEX_VCMPPS_YMM_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_cmp_ps ymm1, ymm2, uvec1, size=4, ext="(IMMEDIATE & mask(5)) |" + YMM
};

def macroop VEX_VCMPPS_YMM_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_cmp_ps ymm1, ymm2, uvec1, size=4, ext="(IMMEDIATE & mask(5)) |" + YMM
};

def macroop VEX_VCMPPD_XMM_XMM_XMM_I {
    gem5_avx_cmp_pd xmm1, xmm2, xmmm, size=8, ext="(IMMEDIATE & mask(5)) |" + XMM
};

def macroop VEX_VCMPPD_XMM_XMM_M_I {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_cmp_pd xmm1, xmm2, uvec1, size=8, ext="(IMMEDIATE & mask(5)) |" + XMM
};

def macroop VEX_VCMPPD_XMM_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_cmp_pd xmm1, xmm2, uvec1, size=8, ext="(IMMEDIATE & mask(5)) |" + XMM
};

def macroop VEX_VCMPPD_YMM_YMM_YMM_I {
    gem5_avx_cmp_pd ymm1, ymm2, ymmm, size=8, ext="(IMMEDIATE & mask(5)) |" + YMM
};

def macroop VEX_VCMPPD_YMM_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_cmp_pd ymm1, ymm2, uvec1, size=8, ext="(IMMEDIATE & mask(5)) |" + YMM
};

def macroop VEX_VCMPPD_YMM_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_cmp_pd ymm1, ymm2, uvec1, size=8, ext="(IMMEDIATE & mask(5)) |" + YMM
};

def macroop VEX_VCMPSD_XMM_XMM_XMM_I {
    gem5_avx_cmp_sd xmm1, xmm2, xmmm, size=8, ext="IMMEDIATE |" + Scalar
};

def macroop VEX_VCMPSD_XMM_XMM_M_I {
    ldvec128lo0 uvec1, seg, sib, "DISPLACEMENT", dataSize=8
    gem5_avx_cmp_sd xmm1, xmm2, uvec1, size=8, ext="IMMEDIATE |" + Scalar
};

def macroop VEX_VCMPSD_XMM_XMM_P_I {
    rdip t7
    ldvec128lo0 ufp1, seg, riprel, "DISPLACEMENT", dataSize=8
    gem5_avx_cmp_sd xmm1, xmm2, uvec1, size=8, ext="IMMEDIATE |" + Scalar
};

'''
