microcode = '''
def macroop INSERTPS_XMM_XMM_I {
    gem5_mm_insert_ps xmm, xmm, xmmm, size=4, ext="IMMEDIATE"
};

def macroop INSERTPS_XMM_M_I {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_mm_insert_ps xmm, xmm, uvec1, size=4, ext="IMMEDIATE"
};

def macroop INSERTPS_XMM_P_I {
    rdip t7
    ldvec128 uvec1, seg, riprel, disp, dataSize=4
    gem5_mm_insert_ps xmm, xmm, uvec1, size=4, ext="IMMEDIATE"
};

def macroop EXTRACTPS_R_XMM_I {
    gem5_mm_extract_psi reg, xmmm, "IMMEDIATE & mask(2)", size=4, ext=0
};

def macroop EXTRACTPS_M_XMM_I {
    gem5_mm_extract_psi t1, xmm, "IMMEDIATE & mask(2)", size=4, ext=0
    st t1, seg, sib, disp, dataSize=4
};

def macroop EXTRACTPS_P_XMM_I {
    rdip t7
    gem5_mm_extract_psi t1, xmm, "IMMEDIATE & mask(2)", size=4, ext=0
    st t1, seg, riprel, disp, dataSize=4
};

'''
