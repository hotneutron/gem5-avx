microcode = '''
def macroop VEX_VMOVMSKPS_R_XMM {
    gem5_avx_movemask_epi32 reg, xmmm, size=4, ext=XMM
};

def macroop VEX_VMOVMSKPS_R_YMM {
    gem5_avx_movemask_epi32 reg, ymmm, size=4, ext=YMM
};

def macroop VEX_VMOVMSKPS_R_M {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VMOVMSKPS_R_P {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VMOVMSKPD_R_XMM {
    gem5_avx_movemask_epi64 reg, xmmm, size=8, ext=XMM
};

def macroop VEX_VMOVMSKPD_R_YMM {
    gem5_avx_movemask_epi64 reg, ymmm, size=8, ext=YMM
};

def macroop VEX_VMOVMSKPD_R_M {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VMOVMSKPD_R_P {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_MASKMOVPS_XMM_XMM_XMM {
    gem5_avx_maskmove_ps xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop VEX_MASKMOVPS_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_maskmove_ps xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_MASKMOVPS_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_maskmove_ps xmm1, xmm2, uvec1, size=4, ext=XMM
};

def macroop VEX_MASKMOVPS_M_XMM_XMM {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_maskmove_ps uvec1, xmm, xmmm, uvec1, size=4, ext=XMM + "| 1"
    stvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop VEX_MASKMOVPS_P_XMM_XMM {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_maskmove_ps uvec1, xmm, xmmm, uvec1, size=4, ext=XMM + "| 1"
    stvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop VEX_MASKMOVPS_YMM_YMM_YMM {
    gem5_avx_maskmove_ps ymm1, ymm2, ymmm, size=4, ext=YMM
};

def macroop VEX_MASKMOVPS_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_maskmove_ps ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_MASKMOVPS_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_maskmove_ps ymm1, ymm2, uvec1, size=4, ext=YMM
};

def macroop VEX_MASKMOVPS_M_YMM_YMM {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_maskmove_ps uvec1, ymm, ymmm, uvec1, size=4, ext=YMM + "| 1"
    stvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
};

def macroop VEX_MASKMOVPS_P_YMM_YMM {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_maskmove_ps uvec1, ymm, ymmm, uvec1, size=4, ext=YMM + "| 1"
    stvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
};

def macroop VEX_MASKMOVPD_XMM_XMM_XMM {
    gem5_avx_maskmove_pd xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop VEX_MASKMOVPD_XMM_XMM_M {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_maskmove_pd xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_MASKMOVPD_XMM_XMM_P {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_maskmove_pd xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_MASKMOVPD_M_XMM_XMM {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_avx_maskmove_pd uvec1, xmm, xmmm, uvec1, size=8, ext=XMM + "| 1"
    stvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop VEX_MASKMOVPD_P_XMM_XMM {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_avx_maskmove_pd uvec1, xmm, xmmm, uvec1, size=8, ext=XMM + "| 1"
    stvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop VEX_MASKMOVPD_YMM_YMM_YMM {
    gem5_avx_maskmove_pd ymm1, ymm2, ymmm, size=8, ext=YMM
};

def macroop VEX_MASKMOVPD_YMM_YMM_M {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_maskmove_pd ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop VEX_MASKMOVPD_YMM_YMM_P {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_maskmove_pd ymm1, ymm2, uvec1, size=8, ext=YMM
};

def macroop VEX_MASKMOVPD_M_YMM_YMM {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_avx_maskmove_pd uvec1, ymm, ymmm, uvec1, size=8, ext=YMM + "| 1"
    stvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
};

def macroop VEX_MASKMOVPD_P_YMM_YMM {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_avx_maskmove_pd uvec1, ymm, ymmm, uvec1, size=8, ext=YMM + " | 1"
    stvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
};

'''
