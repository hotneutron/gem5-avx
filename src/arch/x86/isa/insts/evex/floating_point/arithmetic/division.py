microcode = '''
def macroop EVEX_VDIVSS_XMM_XMM_XMM {
    gem5_avx_div_ss xmm1, xmm2, xmmm, size=4, ext=0
};

def macroop EVEX_VDIVSS_XMM_XMM_M {
    gem5_mm_load_ss uvec1, seg, sib, disp, dataSize=4
    gem5_avx_div_ss xmm1, xmm2, uvec1, size=4, ext=0
};

def macroop EVEX_VDIVSS_XMM_XMM_P {
    rdip t7
    gem5_mm_load_ss uvec1, seg, riprel, disp, dataSize=4
    gem5_avx_div_ss xmm1, xmm2, uvec1, size=4, ext=0
};

def macroop EVEX_VDIVSD_XMM_XMM_XMM {
    gem5_avx_div_sd xmm1, xmm2, xmmm, size=8, ext=0
};

def macroop EVEX_VDIVSD_XMM_XMM_M {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    gem5_avx_div_sd xmm1, xmm2, uvec1, size=8, ext=0
};

def macroop EVEX_VDIVSD_XMM_XMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_div_sd xmm1, xmm2, uvec1, size=8, ext=0
};

def macroop EVEX_VDIVPS_XMM_XMM_XMM {
    gem5_avx_div_ps xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop EVEX_VDIVPS_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_div_ps xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VDIVPS_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_div_ps xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop EVEX_VDIVPS_YMM_YMM_YMM {
    gem5_avx_div_ps ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop EVEX_VDIVPS_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_div_ps ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VDIVPS_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_div_ps ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop EVEX_VDIVPS_ZMM_ZMM_ZMM {
    gem5_avx_div_ps zmm1, zmm2, zmmm, size=4, ext=ZMM
};

def macroop EVEX_VDIVPS_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_div_ps zmm1, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VDIVPS_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_div_ps zmm1, zmm2, uvec1, size=4, ext=ZMM
};

def macroop EVEX_VDIVPD_XMM_XMM_XMM {
    gem5_avx_div_pd xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop EVEX_VDIVPD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_div_pd xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VDIVPD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_div_pd xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop EVEX_VDIVPD_YMM_YMM_YMM {
    gem5_avx_div_pd ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop EVEX_VDIVPD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_div_pd ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VDIVPD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_div_pd ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop EVEX_VDIVPD_ZMM_ZMM_ZMM {
    gem5_avx_div_pd zmm1, zmm2, zmmm, size=8, ext=ZMM
};

def macroop EVEX_VDIVPD_ZMM_ZMM_M {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_avx_div_pd zmm1, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VDIVPD_ZMM_ZMM_P {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_avx_div_pd zmm1, zmm2, uvec1, size=8, ext=ZMM
};

def macroop EVEX_VDIVPS_XMM_XMM_XMM_K {
    gem5_mask_div_ps xmm1, xmm2, xmmm, xmm1, opmask=opmask, size=4, ext=XMM
};

def macroop EVEX_VDIVPS_XMM_XMM_M_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_div_ps xmm1, xmm2, uvec1, xmm1, opmask=opmask, size=4, ext=XMM
};

def macroop EVEX_VDIVPS_XMM_XMM_P_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_div_ps xmm1, xmm2, uvec1, xmm1, opmask=opmask, size=4, ext=XMM
};

def macroop EVEX_VDIVPS_YMM_YMM_YMM_K {
    gem5_mask_div_ps ymm1, ymm2, ymmm, ymm1, opmask=opmask, size=4, ext=YMM
};

def macroop EVEX_VDIVPS_YMM_YMM_M_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_div_ps ymm1, ymm2, uvec1, ymm1, opmask=opmask, size=4, ext=YMM
};

def macroop EVEX_VDIVPS_YMM_YMM_P_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_div_ps ymm1, ymm2, uvec1, ymm1, opmask=opmask, size=4, ext=YMM
};

def macroop EVEX_VDIVPS_ZMM_ZMM_ZMM_K {
    gem5_mask_div_ps zmm1, zmm2, zmmm, zmm1, opmask=opmask, size=4, ext=ZMM
};

def macroop EVEX_VDIVPS_ZMM_ZMM_M_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_div_ps zmm1, zmm2, uvec1, zmm1, opmask=opmask, size=4, ext=ZMM
};

def macroop EVEX_VDIVPS_ZMM_ZMM_P_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_div_ps zmm1, zmm2, uvec1, zmm1, opmask=opmask, size=4, ext=ZMM
};

def macroop EVEX_VDIVPD_XMM_XMM_XMM_K {
    gem5_mask_div_pd xmm1, xmm2, xmmm, xmm1, opmask=opmask, size=8, ext=XMM
};

def macroop EVEX_VDIVPD_XMM_XMM_M_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_div_pd xmm1, xmm2, uvec1, xmm1, opmask=opmask, size=8, ext=XMM
};

def macroop EVEX_VDIVPD_XMM_XMM_P_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_div_pd xmm1, xmm2, uvec1, xmm1, opmask=opmask, size=8, ext=XMM
};

def macroop EVEX_VDIVPD_YMM_YMM_YMM_K {
    gem5_mask_div_pd ymm1, ymm2, ymmm, ymm1, opmask=opmask, size=8, ext=YMM
};

def macroop EVEX_VDIVPD_YMM_YMM_M_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_div_pd ymm1, ymm2, uvec1, ymm1, opmask=opmask, size=8, ext=YMM
};

def macroop EVEX_VDIVPD_YMM_YMM_P_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_div_pd ymm1, ymm2, uvec1, ymm1, opmask=opmask, size=8, ext=YMM
};

def macroop EVEX_VDIVPD_ZMM_ZMM_ZMM_K {
    gem5_mask_div_pd zmm1, zmm2, zmmm, zmm1, opmask=opmask, size=8, ext=ZMM
};

def macroop EVEX_VDIVPD_ZMM_ZMM_M_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_div_pd zmm1, zmm2, uvec1, zmm1, opmask=opmask, size=8, ext=ZMM
};

def macroop EVEX_VDIVPD_ZMM_ZMM_P_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_div_pd zmm1, zmm2, uvec1, zmm1, opmask=opmask, size=8, ext=ZMM
};
'''
