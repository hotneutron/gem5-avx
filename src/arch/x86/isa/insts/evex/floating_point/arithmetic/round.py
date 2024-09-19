microcode = '''
def macroop EVEX_VRNDSCALESS_XMM_XMM_XMM_I {
    gem5_evex_roundscale_ssi xmm1, xmm2, xmmm, imm, size=4, ext=Scalar
};

def macroop EVEX_VRNDSCALESS_XMM_XMM_M_I {
    gem5_mm_load_ss uvec1, seg, sib, disp, dataSize=4
    gem5_evex_roundscale_ssi xmm1, xmm2, uvec1, imm, size=4, ext=Scalar
};

def macroop EVEX_VRNDSCALESS_XMM_XMM_P_I {
    rdip t7
    gem5_mm_load_ss uvec1, seg, riprel, disp, dataSize=4
    gem5_evex_roundscale_ssi xmm1, xmm2, uvec1, imm, size=4, ext=Scalar
};

def macroop EVEX_VRNDSCALESD_XMM_XMM_XMM_I {
    gem5_evex_roundscale_sdi xmm1, xmm2, xmmm, imm, size=8, ext=Scalar
};

def macroop EVEX_VRNDSCALESD_XMM_XMM_M_I {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    gem5_evex_roundscale_sdi xmm1, xmm2, uvec1, imm, size=8, ext=Scalar
};

def macroop EVEX_VRNDSCALESD_XMM_XMM_P_I {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    gem5_evex_roundscale_sdi xmm1, xmm2, uvec1, imm, size=8, ext=Scalar
};

def macroop EVEX_VRNDSCALEPS_XMM_XMM_I {
    gem5_evex_roundscale_psi xmm, xmmm, imm, size=4, ext=XMM
};

def macroop EVEX_VRNDSCALEPS_XMM_M_I {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_evex_roundscale_psi xmm, uvec1, imm, size=4, ext=XMM
};

def macroop EVEX_VRNDSCALEPS_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_evex_roundscale_psi xmm, uvec1, imm, size=4, ext=XMM
};

def macroop EVEX_VRNDSCALEPS_YMM_YMM_I {
    gem5_evex_roundscale_psi ymm, ymmm, imm, size=4, ext=YMM
};

def macroop EVEX_VRNDSCALEPS_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_evex_roundscale_psi ymm, uvec1, imm, size=4, ext=YMM
};

def macroop EVEX_VRNDSCALEPS_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_evex_roundscale_psi ymm, uvec1, imm, size=4, ext=YMM
};

def macroop EVEX_VRNDSCALEPS_ZMM_ZMM_I {
    gem5_evex_roundscale_psi zmm, zmmm, imm, size=4, ext=ZMM
};

def macroop EVEX_VRNDSCALEPS_ZMM_M_I {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_evex_roundscale_psi zmm, uvec1, imm, size=4, ext=ZMM
};

def macroop EVEX_VRNDSCALEPS_ZMM_P_I {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_evex_roundscale_psi zmm, uvec1, imm, size=4, ext=ZMM
};

def macroop EVEX_VRNDSCALEPD_XMM_XMM_I {
    gem5_evex_roundscale_pdi xmm, xmmm, imm, size=8, ext=XMM
};

def macroop EVEX_VRNDSCALEPD_XMM_M_I {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_evex_roundscale_pdi xmm, uvec1, imm, size=8, ext=XMM
};

def macroop EVEX_VRNDSCALEPD_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_evex_roundscale_pdi xmm, uvec1, imm, size=8, ext=XMM
};

def macroop EVEX_VRNDSCALEPD_YMM_YMM_I {
    gem5_evex_roundscale_pdi ymm, ymmm, imm, size=8, ext=YMM
};

def macroop EVEX_VRNDSCALEPD_YMM_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_evex_roundscale_pdi ymm, uvec1, imm, size=8, ext=YMM
};

def macroop EVEX_VRNDSCALEPD_YMM_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_evex_roundscale_pdi ymm, uvec1, imm, size=8, ext=YMM
};

def macroop EVEX_VRNDSCALEPD_ZMM_ZMM_I {
    gem5_evex_roundscale_pdi zmm, zmmm, imm, size=8, ext=ZMM
};

def macroop EVEX_VRNDSCALEPD_ZMM_M_I {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_evex_roundscale_pdi zmm, uvec1, imm, size=8, ext=ZMM
};

def macroop EVEX_VRNDSCALEPD_ZMM_P_I {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_evex_roundscale_pdi zmm, uvec1, imm, size=8, ext=ZMM
};

'''
