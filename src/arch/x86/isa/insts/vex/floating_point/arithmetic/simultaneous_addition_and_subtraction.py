microcode = '''
def macroop VEX_VADDSUBPS_XMM_XMM_XMM {
    gem5_avx_addsub_ps xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop VEX_VADDSUBPS_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_addsub_ps xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VADDSUBPS_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_addsub_ps xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VADDSUBPS_YMM_YMM_YMM {
    gem5_avx_addsub_ps ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop VEX_VADDSUBPS_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_addsub_ps ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VADDSUBPS_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_addsub_ps ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VADDSUBPD_XMM_XMM_XMM {
    gem5_avx_addsub_pd xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop VEX_VADDSUBPD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_addsub_pd xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VADDSUBPD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, sib, disp, dataSize=16
    gem5_avx_addsub_pd xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VADDSUBPD_YMM_YMM_YMM {
    gem5_avx_addsub_pd ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop VEX_VADDSUBPD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_addsub_pd ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop VEX_VADDSUBPD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, sib, disp, dataSize=32
    gem5_avx_addsub_pd ymm1, ymm2, uvec1, size=8, ext=YMM
};
'''
