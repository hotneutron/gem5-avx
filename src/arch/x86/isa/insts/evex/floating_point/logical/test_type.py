microcode = '''
def macroop EVEX_VFPCLASSPD_K_XMM_I {
    gem5_avx_fpclass_pdi k, xmmm, imm, size=8, ext=XMM
};

def macroop EVEX_VFPCLASSPD_K_M_I {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_fpclass_pdi k, uvec1, imm, size=8, ext=XMM
};

def macroop EVEX_VFPCLASSPD_K_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_fpclass_pdi k, uvec1, imm, size=8, ext=XMM
};

def macroop EVEX_VFPCLASSPD_K_YMM_I {
    gem5_avx_fpclass_pdi k, ymmm, imm, size=8, ext=YMM
};

def macroop EVEX_VFPCLASSPD_K_M_I {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_fpclass_pdi k, uvec1, imm, size=8, ext=YMM
};

def macroop EVEX_VFPCLASSPD_K_P_I {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_fpclass_pdi k, uvec1, imm, size=8, ext=YMM
};

def macroop EVEX_VFPCLASSPD_K_ZMM_I {
    gem5_avx_fpclass_pdi k, zmmm, imm, size=8, ext=ZMM
};

def macroop EVEX_VFPCLASSPD_K_M_I {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_fpclass_pdi k, uvec1, imm, size=8, ext=ZMM
};

def macroop EVEX_VFPCLASSPD_K_P_I {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_fpclass_pdi k, uvec1, imm, size=8, ext=ZMM
};

'''
