microcode = '''
def macroop EVEX_VMINSS_XMM_XMM_XMM {
    gem5_avx_min_ss xmm1, xmm2, xmmm, ext=Scalar, size=4
};

def macroop EVEX_VMINSS_XMM_XMM_M {
    gem5_mm_load_ss uvec1, seg, sib, "DISPLACEMENT", dataSize=4
    gem5_avx_min_ss xmm1, xmm2, uvec1, ext=Scalar, size=4
};

def macroop EVEX_VMINSS_XMM_XMM_P {
    rdip t7
    gem5_mm_load_ss uvec1, seg, riprel, "DISPLACEMENT", dataSize=4
    gem5_avx_min_ss xmm1, xmm2, uvec1, ext=Scalar, size=4
};

def macroop EVEX_VMINSD_XMM_XMM_XMM {
    gem5_avx_min_sd xmm1, xmm2, xmmm, ext=Scalar, size=8
};

def macroop EVEX_VMINSD_XMM_XMM_M {
    ldvec128lo0 uvec1, seg, sib, "DISPLACEMENT", dataSize=8
    gem5_avx_min_sd xmm1, xmm2, uvec1, ext=Scalar, size=8
};

def macroop EVEX_VMINSD_XMM_XMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, "DISPLACEMENT", dataSize=8
    gem5_avx_min_sd xmm1, xmm2, uvec1, ext=Scalar, size=8
};

def macroop EVEX_VMINPS_XMM_XMM_XMM {
    gem5_avx_min_ps xmm1, xmm2, xmmm, ext=XMM, size=4
};

def macroop EVEX_VMINPS_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_min_ps xmm1, xmm2, uvec1, ext=XMM, size=4
};

def macroop EVEX_VMINPS_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_min_ps xmm1, xmm2, uvec1, ext=XMM, size=4
};

def macroop EVEX_VMINPS_YMM_YMM_YMM {
    gem5_avx_min_ps ymm1, ymm2, ymmm, ext=YMM, size=4
};

def macroop EVEX_VMINPS_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_min_ps ymm1, ymm2, uvec1, ext=YMM, size=4
};

def macroop EVEX_VMINPS_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_min_ps ymm1, ymm2, uvec1, ext=YMM, size=4
};

def macroop EVEX_VMINPS_ZMM_ZMM_ZMM {
    gem5_avx_min_ps zmm1, zmm2, zmmm, ext=ZMM, size=4
};

def macroop EVEX_VMINPS_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_min_ps zmm1, zmm2, uvec1, ext=ZMM, size=4
};

def macroop EVEX_VMINPS_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_min_ps zmm1, zmm2, uvec1, ext=ZMM, size=4
};

def macroop EVEX_VMINPD_XMM_XMM_XMM {
    gem5_avx_min_pd xmm1, xmm2, xmmm, ext=XMM, size=8
};

def macroop EVEX_VMINPD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_min_pd xmm1, xmm2, uvec1, ext=XMM, size=8
};

def macroop EVEX_VMINPD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_min_pd xmm1, xmm2, uvec1, ext=XMM, size=8
};

def macroop EVEX_VMINPD_YMM_YMM_YMM {
    gem5_avx_min_pd ymm1, ymm2, ymmm, ext=YMM, size=8
};

def macroop EVEX_VMINPD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_min_pd ymm1, ymm2, uvec1, ext=YMM, size=8
};

def macroop EVEX_VMINPD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_min_pd ymm1, ymm2, uvec1, ext=YMM, size=8
};

def macroop EVEX_VMINPD_ZMM_ZMM_ZMM {
    gem5_avx_min_pd zmm1, zmm2, zmmm, ext=ZMM, size=8
};

def macroop EVEX_VMINPD_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_min_pd zmm1, zmm2, uvec1, ext=ZMM, size=8
};

def macroop EVEX_VMINPD_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_min_pd zmm1, zmm2, uvec1, ext=ZMM, size=8
};

def macroop EVEX_VMINPS_XMM_XMM_XMM_K {
    gem5_mask_min_ps xmm1, xmm2, xmmm, xmm1, opmask=opmask, size=4, ext=XMM
};

def macroop EVEX_VMINPS_XMM_XMM_M_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_min_ps xmm1, xmm2, uvec1, xmm1, opmask=opmask, size=4, ext=XMM
};

def macroop EVEX_VMINPS_XMM_XMM_P_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_min_ps xmm1, xmm2, uvec1, xmm1, opmask=opmask, size=4, ext=XMM
};

def macroop EVEX_VMINPS_YMM_YMM_YMM_K {
    gem5_mask_min_ps ymm1, ymm2, ymmm, ymm1, opmask=opmask, size=4, ext=YMM
};

def macroop EVEX_VMINPS_YMM_YMM_M_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_min_ps ymm1, ymm2, uvec1, ymm1, opmask=opmask, size=4, ext=YMM
};

def macroop EVEX_VMINPS_YMM_YMM_P_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_min_ps ymm1, ymm2, uvec1, ymm1, opmask=opmask, size=4, ext=YMM
};

def macroop EVEX_VMINPS_ZMM_ZMM_ZMM_K {
    gem5_mask_min_ps zmm1, zmm2, zmmm, zmm1, opmask=opmask, size=4, ext=ZMM
};

def macroop EVEX_VMINPS_ZMM_ZMM_M_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_min_ps zmm1, zmm2, uvec1, zmm1, opmask=opmask, size=4, ext=ZMM
};

def macroop EVEX_VMINPS_ZMM_ZMM_P_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_min_ps zmm1, zmm2, uvec1, zmm1, opmask=opmask, size=4, ext=ZMM
};

def macroop EVEX_VMINPD_XMM_XMM_XMM_K {
    gem5_mask_min_pd xmm1, xmm2, xmmm, xmm1, opmask=opmask, size=8, ext=XMM
};

def macroop EVEX_VMINPD_XMM_XMM_M_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_min_pd xmm1, xmm2, uvec1, xmm1, opmask=opmask, size=8, ext=XMM
};

def macroop EVEX_VMINPD_XMM_XMM_P_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_min_pd xmm1, xmm2, uvec1, xmm1, opmask=opmask, size=8, ext=XMM
};

def macroop EVEX_VMINPD_YMM_YMM_YMM_K {
    gem5_mask_min_pd ymm1, ymm2, ymmm, ymm1, opmask=opmask, size=8, ext=YMM
};

def macroop EVEX_VMINPD_YMM_YMM_M_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_min_pd ymm1, ymm2, uvec1, ymm1, opmask=opmask, size=8, ext=YMM
};

def macroop EVEX_VMINPD_YMM_YMM_P_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_min_pd ymm1, ymm2, uvec1, ymm1, opmask=opmask, size=8, ext=YMM
};

def macroop EVEX_VMINPD_ZMM_ZMM_ZMM_K {
    gem5_mask_min_pd zmm1, zmm2, zmmm, zmm1, opmask=opmask, size=8, ext=ZMM
};

def macroop EVEX_VMINPD_ZMM_ZMM_M_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_min_pd zmm1, zmm2, uvec1, zmm1, opmask=opmask, size=8, ext=ZMM
};

def macroop EVEX_VMINPD_ZMM_ZMM_P_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_min_pd zmm1, zmm2, uvec1, zmm1, opmask=opmask, size=8, ext=ZMM
};

def macroop EVEX_VMAXSS_XMM_XMM_XMM {
    gem5_avx_max_ss xmm1, xmm2, xmmm, ext=Scalar, size=4
};

def macroop EVEX_VMAXSS_XMM_XMM_M {
    gem5_mm_load_ss uvec1, seg, sib, "DISPLACEMENT", dataSize=4
    gem5_avx_max_ss xmm1, xmm2, uvec1, ext=Scalar, size=4
};

def macroop EVEX_VMAXSS_XMM_XMM_P {
    rdip t7
    gem5_mm_load_ss uvec1, seg, riprel, "DISPLACEMENT", dataSize=4
    gem5_avx_max_ss xmm1, xmm2, uvec1, ext=Scalar, size=4
};

def macroop EVEX_VMAXSD_XMM_XMM_XMM {
    gem5_avx_max_sd xmm1, xmm2, xmmm, ext=Scalar, size=8
};

def macroop EVEX_VMAXSD_XMM_XMM_M {
    ldvec128lo0 uvec1, seg, sib, "DISPLACEMENT", dataSize=8
    gem5_avx_max_sd xmm1, xmm2, uvec1, ext=Scalar, size=8
};

def macroop EVEX_VMAXSD_XMM_XMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, "DISPLACEMENT", dataSize=8
    gem5_avx_max_sd xmm1, xmm2, uvec1, ext=Scalar, size=8
};

def macroop EVEX_VMAXPS_XMM_XMM_XMM {
    gem5_avx_max_ps xmm1, xmm2, xmmm, ext=XMM, size=4
};

def macroop EVEX_VMAXPS_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_max_ps xmm1, xmm2, uvec1, ext=XMM, size=4
};

def macroop EVEX_VMAXPS_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_max_ps xmm1, xmm2, uvec1, ext=XMM, size=4
};

def macroop EVEX_VMAXPS_YMM_YMM_YMM {
    gem5_avx_max_ps ymm1, ymm2, ymmm, ext=YMM, size=4
};

def macroop EVEX_VMAXPS_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_max_ps ymm1, ymm2, uvec1, ext=YMM, size=4
};

def macroop EVEX_VMAXPS_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_max_ps ymm1, ymm2, uvec1, ext=YMM, size=4
};

def macroop EVEX_VMAXPS_ZMM_ZMM_ZMM {
    gem5_avx_max_ps zmm1, zmm2, zmmm, ext=ZMM, size=4
};

def macroop EVEX_VMAXPS_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_max_ps zmm1, zmm2, uvec1, ext=ZMM, size=4
};

def macroop EVEX_VMAXPS_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_max_ps zmm1, zmm2, uvec1, ext=ZMM, size=4
};

def macroop EVEX_VMAXPD_XMM_XMM_XMM {
    gem5_avx_max_pd xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop EVEX_VMAXPD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_max_pd xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VMAXPD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_max_pd xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VMAXPD_YMM_YMM_YMM {
    gem5_avx_max_pd ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop EVEX_VMAXPD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_max_pd ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VMAXPD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_max_pd ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VMAXPD_ZMM_ZMM_ZMM {
    gem5_avx_max_pd zmm1, zmm2, zmmm, size=8, ext=ZMM
};

def macroop EVEX_VMAXPD_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_max_pd zmm1, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VMAXPD_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_max_pd zmm1, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VMAXPS_XMM_XMM_XMM_K {
    gem5_mask_max_ps xmm1, xmm2, xmmm, xmm1, opmask=opmask, size=4, ext=XMM
};

def macroop EVEX_VMAXPS_XMM_XMM_M_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_max_ps xmm1, xmm2, uvec1, xmm1, opmask=opmask, size=4, ext=XMM
};

def macroop EVEX_VMAXPS_XMM_XMM_P_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_max_ps xmm1, xmm2, uvec1, xmm1, opmask=opmask, size=4, ext=XMM
};

def macroop EVEX_VMAXPS_YMM_YMM_YMM_K {
    gem5_mask_max_ps ymm1, ymm2, ymmm, ymm1, opmask=opmask, size=4, ext=YMM
};

def macroop EVEX_VMAXPS_YMM_YMM_M_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_max_ps ymm1, ymm2, uvec1, ymm1, opmask=opmask, size=4, ext=YMM
};

def macroop EVEX_VMAXPS_YMM_YMM_P_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_max_ps ymm1, ymm2, uvec1, ymm1, opmask=opmask, size=4, ext=YMM
};

def macroop EVEX_VMAXPS_ZMM_ZMM_ZMM_K {
    gem5_mask_max_ps zmm1, zmm2, zmmm, zmm1, opmask=opmask, size=4, ext=ZMM
};

def macroop EVEX_VMAXPS_ZMM_ZMM_M_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_max_ps zmm1, zmm2, uvec1, zmm1, opmask=opmask, size=4, ext=ZMM
};

def macroop EVEX_VMAXPS_ZMM_ZMM_P_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_max_ps zmm1, zmm2, uvec1, zmm1, opmask=opmask, size=4, ext=ZMM
};

def macroop EVEX_VMAXPD_XMM_XMM_XMM_K {
    gem5_mask_max_pd xmm1, xmm2, xmmm, xmm1, opmask=opmask, size=8, ext=XMM
};

def macroop EVEX_VMAXPD_XMM_XMM_M_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_max_pd xmm1, xmm2, uvec1, xmm1, opmask=opmask, size=8, ext=XMM
};

def macroop EVEX_VMAXPD_XMM_XMM_P_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_max_pd xmm1, xmm2, uvec1, xmm1, opmask=opmask, size=8, ext=XMM
};

def macroop EVEX_VMAXPD_YMM_YMM_YMM_K {
    gem5_mask_max_pd ymm1, ymm2, ymmm, ymm1, opmask=opmask, size=8, ext=YMM
};

def macroop EVEX_VMAXPD_YMM_YMM_M_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_max_pd ymm1, ymm2, uvec1, ymm1, opmask=opmask, size=8, ext=YMM
};

def macroop EVEX_VMAXPD_YMM_YMM_P_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_max_pd ymm1, ymm2, uvec1, ymm1, opmask=opmask, size=8, ext=YMM
};

def macroop EVEX_VMAXPD_ZMM_ZMM_ZMM_K {
    gem5_mask_max_pd zmm1, zmm2, zmmm, zmm1, opmask=opmask, size=8, ext=ZMM
};

def macroop EVEX_VMAXPD_ZMM_ZMM_M_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_max_pd zmm1, zmm2, uvec1, zmm1, opmask=opmask, size=8, ext=ZMM
};

def macroop EVEX_VMAXPD_ZMM_ZMM_P_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_max_pd zmm1, zmm2, uvec1, zmm1, opmask=opmask, size=8, ext=ZMM
};

'''
