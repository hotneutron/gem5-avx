microcode = '''
def macroop VEX_VRCPSS_XMM_XMM_XMM {
    gem5_mm256_rcp_ss xmm1, xmm2, xmmm, size=4, ext=Scalar
};

def macroop VEX_VRCPSS_XMM_XMM_M {
    gem5_mm_load_ss uvec1, seg, sib, disp, dataSize=4
    gem5_mm256_rcp_ss xmm1, xmm2, uvec1, size=4, ext=Scalar
};

def macroop VEX_VRCPSS_XMM_XMM_P {
    rdip t7
    gem5_mm_load_ss uvec1, seg, riprel, disp, dataSize=4
    gem5_mm256_rcp_ss xmm1, xmm2, uvec1, size=4, ext=Scalar
};

def macroop VEX_VRCPPS_XMM_XMM {
    gem5_mm256_rcp_ps xmm, xmmm, size=4, ext=XMM
};

def macroop VEX_VRCPPS_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mm256_rcp_ps xmm, uvec1, size=4, ext=XMM
};

def macroop VEX_VRCPPS_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mm256_rcp_ps xmm, uvec1, size=4, ext=XMM
};

def macroop VEX_VRCPPS_YMM_YMM {
    gem5_mm256_rcp_ps ymm, ymmm, size=4, ext=YMM
};

def macroop VEX_VRCPPS_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mm256_rcp_ps ymm, uvec1, size=4, ext=YMM
};

def macroop VEX_VRCPPS_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mm256_rcp_ps ymm, uvec1, size=4, ext=YMM
};

'''
