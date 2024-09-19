microcode = '''
def macroop VEX_VDPPS_XMM_XMM_XMM_I {
    gem5_avx_dp_ps xmm1, xmm2, xmmm, size=4, ext = "IMMEDIATE |" + XMM
};

def macroop VEX_VDPPS_XMM_XMM_M_I {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_dp_ps xmm1, xmm2, uvec1, size=4, ext = "IMMEDIATE |" + XMM
};

def macroop VEX_VDPPS_XMM_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_dp_ps xmm1, xmm2, uvec1, size=4, ext = "IMMEDIATE |" + XMM
};

def macroop VEX_VDPPS_YMM_YMM_YMM_I {
    gem5_avx_dp_ps ymm1, ymm2, ymmm, size=4, ext = "IMMEDIATE |" + YMM
};

def macroop VEX_VDPPS_YMM_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_dp_ps ymm1, ymm2, uvec1, size=4, ext = "IMMEDIATE |" + YMM
};

def macroop VEX_VDPPS_YMM_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_dp_ps ymm1, ymm2, uvec1, size=4, ext = "IMMEDIATE |" + YMM
};

def macroop VEX_VDPPD_XMM_XMM_XMM_I {
    gem5_avx_dp_pd xmm1, xmm2, xmmm, size=4, ext = "IMMEDIATE |" + XMM
};

def macroop VEX_VDPPD_XMM_XMM_M_I {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_dp_pd xmm1, xmm2, uvec1, size=4, ext = "IMMEDIATE |" + XMM
};

def macroop VEX_VDPPD_XMM_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_dp_pd xmm1, xmm2, uvec1, size=4, ext = "IMMEDIATE |" + XMM
};

'''
