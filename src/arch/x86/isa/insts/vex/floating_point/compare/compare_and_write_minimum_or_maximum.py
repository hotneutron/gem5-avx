microcode = '''
def macroop VEX_VMINSS_XMM_XMM_XMM {
    gem5_avx_min_ss xmm1, xmm2, xmmm, ext=Scalar, size=4
};

def macroop VEX_VMINSS_XMM_XMM_M {
    gem5_mm_load_ss uvec1, seg, sib, "DISPLACEMENT", dataSize=4
    gem5_avx_min_ss xmm1, xmm2, uvec1, ext=Scalar, size=4
};

def macroop VEX_VMINSS_XMM_XMM_P {
    rdip t7
    gem5_mm_load_ss uvec1, seg, riprel, "DISPLACEMENT", dataSize=4
    gem5_avx_min_ss xmm1, xmm2, uvec1, ext=Scalar, size=4
};

def macroop VEX_VMINSD_XMM_XMM_XMM {
    gem5_avx_min_sd xmm1, xmm2, xmmm, ext=Scalar, size=8
};

def macroop VEX_VMINSD_XMM_XMM_M {
    ldvec128lo0 uvec1, seg, sib, "DISPLACEMENT", dataSize=8
    gem5_avx_min_sd xmm1, xmm2, uvec1, ext=Scalar, size=8
};

def macroop VEX_VMINSD_XMM_XMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, "DISPLACEMENT", dataSize=8
    gem5_avx_min_sd xmm1, xmm2, uvec1, ext=Scalar, size=8
};

def macroop VEX_VMINPS_XMM_XMM_XMM {
    gem5_avx_min_ps xmm1, xmm2, xmmm, ext=XMM, size=4
};

def macroop VEX_VMINPS_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_min_ps xmm1, xmm2, uvec1, ext=XMM, size=4
};

def macroop VEX_VMINPS_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_min_ps xmm1, xmm2, uvec1, ext=XMM, size=4
};

def macroop VEX_VMINPS_YMM_YMM_YMM {
    gem5_avx_min_ps ymm1, ymm2, ymmm, ext=YMM, size=4
};

def macroop VEX_VMINPS_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_min_ps ymm1, ymm2, uvec1, ext=YMM, size=4
};

def macroop VEX_VMINPS_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_min_ps ymm1, ymm2, uvec1, ext=YMM, size=4
};

def macroop VEX_VMINPD_XMM_XMM_XMM {
    gem5_avx_min_pd xmm1, xmm2, xmmm, ext=XMM, size=8
};

def macroop VEX_VMINPD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_min_pd xmm1, xmm2, uvec1, ext=XMM, size=8
};

def macroop VEX_VMINPD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_min_pd xmm1, xmm2, uvec1, ext=XMM, size=8
};

def macroop VEX_VMINPD_YMM_YMM_YMM {
    gem5_avx_min_pd ymm1, ymm2, ymmm, ext=YMM, size=8
};

def macroop VEX_VMINPD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_min_pd ymm1, ymm2, uvec1, ext=YMM, size=8
};

def macroop VEX_VMINPD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_min_pd ymm1, ymm2, uvec1, ext=YMM, size=8
};

def macroop VEX_VMAXSS_XMM_XMM_XMM {
    gem5_avx_max_ss xmm1, xmm2, xmmm, ext=Scalar, size=4
};

def macroop VEX_VMAXSS_XMM_XMM_M {
    gem5_mm_load_ss uvec1, seg, sib, "DISPLACEMENT", dataSize=4
    gem5_avx_max_ss xmm1, xmm2, uvec1, ext=Scalar, size=4
};

def macroop VEX_VMAXSS_XMM_XMM_P {
    rdip t7
    gem5_mm_load_ss uvec1, seg, riprel, "DISPLACEMENT", dataSize=4
    gem5_avx_max_ss xmm1, xmm2, uvec1, ext=Scalar, size=4
};

def macroop VEX_VMAXSD_XMM_XMM_XMM {
    gem5_avx_max_sd xmm1, xmm2, xmmm, ext=Scalar, size=8
};

def macroop VEX_VMAXSD_XMM_XMM_M {
    ldvec128lo0 uvec1, seg, sib, "DISPLACEMENT", dataSize=8
    gem5_avx_max_sd xmm1, xmm2, uvec1, ext=Scalar, size=8
};

def macroop VEX_VMAXSD_XMM_XMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, "DISPLACEMENT", dataSize=8
    gem5_avx_max_sd xmm1, xmm2, uvec1, ext=Scalar, size=8
};

def macroop VEX_VMAXPS_XMM_XMM_XMM {
    gem5_avx_max_ps xmm1, xmm2, xmmm, ext=XMM, size=4
};

def macroop VEX_VMAXPS_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_max_ps xmm1, xmm2, uvec1, ext=XMM, size=4
};

def macroop VEX_VMAXPS_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_max_ps xmm1, xmm2, uvec1, ext=XMM, size=4
};

def macroop VEX_VMAXPS_YMM_YMM_YMM {
    gem5_avx_max_ps ymm1, ymm2, ymmm, ext=YMM, size=4
};

def macroop VEX_VMAXPS_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_max_ps ymm1, ymm2, uvec1, ext=YMM, size=4
};

def macroop VEX_VMAXPS_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_max_ps ymm1, ymm2, uvec1, ext=YMM, size=4
};

def macroop VEX_VMAXPD_XMM_XMM_XMM {
    gem5_avx_max_pd xmm1, xmm2, xmmm, ext=XMM, size=8
};

def macroop VEX_VMAXPD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_max_pd xmm1, xmm2, uvec1, ext=XMM, size=8
};

def macroop VEX_VMAXPD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_max_pd xmm1, xmm2, uvec1, ext=XMM, size=8
};

def macroop VEX_VMAXPD_YMM_YMM_YMM {
    gem5_avx_max_pd ymm1, ymm2, ymmm, ext=YMM, size=8
};

def macroop VEX_VMAXPD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_max_pd ymm1, ymm2, uvec1, ext=YMM, size=8
};

def macroop VEX_VMAXPD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_max_pd ymm1, ymm2, uvec1, ext=YMM, size=8
};
'''
