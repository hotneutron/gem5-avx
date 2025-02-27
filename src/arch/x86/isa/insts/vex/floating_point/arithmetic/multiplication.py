microcode = '''
def macroop VEX_VMULSS_XMM_XMM_XMM {
    gem5_avx_mul_ss xmm1, xmm2, xmmm, size=4, ext=0
};

def macroop VEX_VMULSS_XMM_XMM_M {
    gem5_mm_load_ss uvec1, seg, sib, disp, dataSize=4
    gem5_avx_mul_ss xmm1, xmm2, uvec1, size=4, ext=0
};

def macroop VEX_VMULSS_XMM_XMM_P {
    rdip t7
    gem5_mm_load_ss uvec1, seg, riprel, disp, dataSize=4
    gem5_avx_mul_ss xmm1, xmm2, uvec1, size=4, ext=0
};

def macroop VEX_VMULSD_XMM_XMM_XMM {
    gem5_avx_mul_sd xmm1, xmm2, xmmm, size=8, ext=0
};

def macroop VEX_VMULSD_XMM_XMM_M {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    gem5_avx_mul_sd xmm1, xmm2, uvec1, size=8, ext=0
};

def macroop VEX_VMULSD_XMM_XMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_mul_sd xmm1, xmm2, uvec1, size=8, ext=0
};

def macroop VEX_VMULPS_XMM_XMM_XMM {
    gem5_avx_mul_ps xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop VEX_VMULPS_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_mul_ps xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VMULPS_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_mul_ps xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_VMULPD_XMM_XMM_XMM {
    gem5_avx_mul_pd xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop VEX_VMULPD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_mul_pd xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VMULPD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_mul_pd xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VMULPS_YMM_YMM_YMM {
    gem5_avx_mul_ps ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop VEX_VMULPS_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_mul_ps ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VMULPS_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_mul_ps ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_VMULPD_YMM_YMM_YMM {
    gem5_avx_mul_pd ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop VEX_VMULPD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_mul_pd ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop VEX_VMULPD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_mul_pd ymm1, ymm2, uvec1, size=8, ext=YMM
};

'''
