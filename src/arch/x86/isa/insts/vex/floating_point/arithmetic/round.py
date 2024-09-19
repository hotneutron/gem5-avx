microcode = '''
def macroop VEX_VROUNDSS_XMM_XMM_XMM_I {
    gem5_avx_round_ssi xmm1, xmm2, xmmm, imm, size=4, ext=Scalar
};

def macroop VEX_VROUNDSS_XMM_XMM_M_I {
    gem5_mm_load_ss uvec1, seg, sib, disp, dataSize=4
    gem5_avx_round_ssi xmm1, xmm2, uvec1, imm, size=4, ext=Scalar
};

def macroop VEX_VROUNDSS_XMM_XMM_P_I {
    rdip t7
    gem5_mm_load_ss uvec1, seg, riprel, disp, dataSize=4
    gem5_avx_round_ssi xmm1, xmm2, uvec1, imm, size=4, ext=Scalar
};

def macroop VEX_VROUNDSD_XMM_XMM_XMM_I {
    gem5_avx_round_sdi xmm1, xmm2, xmmm, imm, size=8, ext=Scalar
};

def macroop VEX_VROUNDSD_XMM_XMM_M_I {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    gem5_avx_round_sdi xmm1, xmm2, uvec1, imm, size=8, ext=Scalar
};

def macroop VEX_VROUNDSD_XMM_XMM_P_I {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_round_sdi xmm1, xmm2, uvec1, imm, size=8, ext=Scalar
};

def macroop VEX_VROUNDPS_XMM_XMM_I {
    gem5_avx_round_psi xmm, xmmm, imm, size=4, ext=XMM
};

def macroop VEX_VROUNDPS_XMM_M_I {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_round_psi xmm, uvec1, imm, size=4, ext=XMM
};

def macroop VEX_VROUNDPS_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_round_psi xmm, uvec1, imm, size=4, ext=XMM
};

def macroop VEX_VROUNDPS_YMM_YMM_I {
    gem5_avx_round_psi ymm, ymmm, imm, size=4, ext=YMM
};

def macroop VEX_VROUNDPS_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_round_psi ymm, uvec1, imm, size=4, ext=YMM
};

def macroop VEX_VROUNDPS_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_round_psi ymm, uvec1, imm, size=4, ext=YMM
};

def macroop VEX_VROUNDPD_XMM_XMM_I {
    gem5_avx_round_pdi xmm, xmmm, imm, size=8, ext=XMM
};

def macroop VEX_VROUNDPD_XMM_M_I {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_round_pdi xmm, uvec1, imm, size=8, ext=XMM
};

def macroop VEX_VROUNDPD_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_round_pdi xmm, uvec1, imm, size=8, ext=XMM
};

def macroop VEX_VROUNDPD_YMM_YMM_I {
    gem5_avx_round_pdi ymm, ymmm, imm, size=8, ext=YMM
};

def macroop VEX_VROUNDPD_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_round_pdi ymm, uvec1, imm, size=8, ext=YMM
};

def macroop VEX_VROUNDPD_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_round_pdi ymm, uvec1, imm, size=8, ext=YMM
};

'''
