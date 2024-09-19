microcode = '''
def macroop EVEX_VCMPPS_K_XMM_XMM_I {
    gem5_evex_cmp_ps k, xmm2, xmmm, size=4, ext="(IMMEDIATE & mask(5)) |" + XMM
};

def macroop EVEX_VCMPPS_K_XMM_M_I {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_evex_cmp_ps k, xmm2, uvec1, size=4, ext="(IMMEDIATE & mask(5)) |" + XMM
};

def macroop EVEX_VCMPPS_K_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_evex_cmp_ps k, xmm2, uvec1, size=4, ext="(IMMEDIATE & mask(5)) |" + XMM
};

def macroop EVEX_VCMPPS_K_YMM_YMM_I {
    gem5_evex_cmp_ps k, ymm2, ymmm, size=4, ext="(IMMEDIATE & mask(5)) |" + YMM
};

def macroop EVEX_VCMPPS_K_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_evex_cmp_ps k, ymm2, uvec1, size=4, ext="(IMMEDIATE & mask(5)) |" + YMM
};

def macroop EVEX_VCMPPS_K_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_evex_cmp_ps k, ymm2, uvec1, size=4, ext="(IMMEDIATE & mask(5)) |" + YMM
};

def macroop EVEX_VCMPPS_K_ZMM_ZMM_I {
    gem5_evex_cmp_ps k, zmm2, zmmm, size=4, ext="(IMMEDIATE & mask(5)) |" + ZMM
};

def macroop EVEX_VCMPPS_K_ZMM_M_I {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_evex_cmp_ps k, zmm2, uvec1, size=4, ext="(IMMEDIATE & mask(5)) |" + ZMM
};

def macroop EVEX_VCMPPS_K_ZMM_P_I {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_evex_cmp_ps k, zmm2, uvec1, size=4, ext="(IMMEDIATE & mask(5)) |" + ZMM
};

def macroop EVEX_VCMPPD_K_XMM_XMM_I {
    gem5_evex_cmp_pd k, xmm2, xmmm, size=8, ext="(IMMEDIATE & mask(5)) |" + XMM
};

def macroop EVEX_VCMPPD_K_XMM_M_I {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_evex_cmp_pd k, xmm2, uvec1, size=8, ext="(IMMEDIATE & mask(5)) |" + XMM
};

def macroop EVEX_VCMPPD_K_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_evex_cmp_pd k, xmm2, uvec1, size=8, ext="(IMMEDIATE & mask(5)) |" + XMM
};

def macroop EVEX_VCMPPD_K_YMM_YMM_I {
    gem5_evex_cmp_pd k, ymm2, ymmm, size=8, ext="(IMMEDIATE & mask(5)) |" + YMM
};

def macroop EVEX_VCMPPD_K_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_evex_cmp_pd k, ymm2, uvec1, size=8, ext="(IMMEDIATE & mask(5)) |" + YMM
};

def macroop EVEX_VCMPPD_K_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_evex_cmp_pd k, ymm2, uvec1, size=8, ext="(IMMEDIATE & mask(5)) |" + YMM
};

def macroop EVEX_VCMPPD_K_ZMM_ZMM_I {
    gem5_evex_cmp_pd k, zmm2, zmmm, size=8, ext="(IMMEDIATE & mask(5)) |" + ZMM
};

def macroop EVEX_VCMPPD_K_ZMM_M_I {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_evex_cmp_pd k, zmm2, uvec1, size=8, ext="(IMMEDIATE & mask(5)) |" + ZMM
};

def macroop EVEX_VCMPPD_K_ZMM_P_I {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_evex_cmp_pd k, zmm2, uvec1, size=8, ext="(IMMEDIATE & mask(5)) |" + ZMM
};

def macroop EVEX_VCMPPD_K_XMM_XMM_I_K {
    gem5_mask_cmp_pd k, xmm2, xmmm, opmask=opmask, size=8, ext="(IMMEDIATE & mask(5)) |" + XMM
};

def macroop EVEX_VCMPPD_K_XMM_M_I_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_cmp_pd k, xmm2, uvec1, opmask=opmask, size=8, ext="(IMMEDIATE & mask(5)) |" + XMM
};

def macroop EVEX_VCMPPD_K_XMM_P_I_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_cmp_pd k, xmm2, uvec1, opmask=opmask, size=8, ext="(IMMEDIATE & mask(5)) |" + XMM
};

def macroop EVEX_VCMPPD_K_YMM_YMM_I_K {
    gem5_mask_cmp_pd k, ymm2, ymmm, opmask=opmask, size=8, ext="(IMMEDIATE & mask(5)) |" + YMM
};

def macroop EVEX_VCMPPD_K_YMM_M_I_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_cmp_pd k, ymm2, uvec1, opmask=opmask, size=8, ext="(IMMEDIATE & mask(5)) |" + YMM
};

def macroop EVEX_VCMPPD_K_YMM_P_I_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_cmp_pd k, ymm2, uvec1, opmask=opmask, size=8, ext="(IMMEDIATE & mask(5)) |" + YMM
};

def macroop EVEX_VCMPPD_K_ZMM_ZMM_I_K {
    gem5_mask_cmp_pd k, zmm2, zmmm, opmask=opmask, size=8, ext="(IMMEDIATE & mask(5)) |" + ZMM
};

def macroop EVEX_VCMPPD_K_ZMM_M_I_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_cmp_pd k, zmm2, uvec1, opmask=opmask, size=8, ext="(IMMEDIATE & mask(5)) |" + ZMM
};

def macroop EVEX_VCMPPD_K_ZMM_P_I_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_cmp_pd k, zmm2, uvec1, opmask=opmask, size=8, ext="(IMMEDIATE & mask(5)) |" + ZMM
};

'''
