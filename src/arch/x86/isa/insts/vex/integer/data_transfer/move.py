microcode = '''
def macroop VEX_KMOVB_K_K {
    gem5_moveto_opmask k, km, size=1, ext=1
};

def macroop VEX_KMOVB_K_M {
    ldmask umask1, seg, sib, disp, dataSize=1
    gem5_moveto_opmask k, umask1, size=1, ext=1
};

def macroop VEX_KMOVB_K_P {
    rdip t7
    ldmask umask1, seg, riprel, disp, dataSize=1
    gem5_moveto_opmask k, umask1, size=1, ext=1
};

def macroop VEX_KMOVB_M_K {
    gem5_movefrom_opmask t1, k, size=1, ext=0
    st t1, seg, sib, disp, dataSize=1
};

def macroop VEX_KMOVB_P_K {
    gem5_movefrom_opmask t1, k, size=1, ext=0
    rdip t7
    st t1, seg, riprel, disp, dataSize=1
};

def macroop VEX_KMOVB_K_R {
    gem5_moveto_opmask k, regm, size=1, ext=0
};

def macroop VEX_KMOVB_R_K {
    gem5_movefrom_opmask reg, km, size=1, ext=0
};

def macroop VEX_KMOVB_R_M {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_KMOVB_R_P {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_KMOVW_K_K {
    gem5_moveto_opmask k, km, size=2, ext=1
};

def macroop VEX_KMOVW_K_M {
    ldmask umask1, seg, sib, disp, dataSize=2
    gem5_moveto_opmask k, umask1, size=2, ext=1
};

def macroop VEX_KMOVW_K_P {
    rdip t7
    ldmask umask1, seg, riprel, disp, dataSize=2
    gem5_moveto_opmask k, umask1, size=2, ext=1
};

def macroop VEX_KMOVW_M_K {
    gem5_movefrom_opmask t1, k, size=2, ext=0
    st t1, seg, sib, disp, dataSize=2
};

def macroop VEX_KMOVW_P_K {
    gem5_movefrom_opmask t1, k, size=2, ext=0
    rdip t7
    st t1, seg, riprel, disp, dataSize=2
};

def macroop VEX_KMOVW_K_R {
    gem5_moveto_opmask k, regm, size=2, ext=0
};

def macroop VEX_KMOVW_R_K {
    gem5_movefrom_opmask reg, km, size=2, ext=0
};

def macroop VEX_KMOVW_R_M {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_KMOVW_R_P {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_KMOVD_K_K {
    gem5_moveto_opmask k, km, size=4, ext=1
};

def macroop VEX_KMOVD_K_M {
    ldmask umask1, seg, sib, disp, dataSize=4
    gem5_moveto_opmask k, umask1, size=4, ext=1
};

def macroop VEX_KMOVD_K_P {
    rdip t7
    ldmask umask1, seg, riprel, disp, dataSize=4
    gem5_moveto_opmask k, umask1, size=4, ext=1
};

def macroop VEX_KMOVD_K_R {
    gem5_moveto_opmask k, regm, size=4, ext=0
};

def macroop VEX_KMOVD_R_K {
    gem5_movefrom_opmask reg, km, size=4, ext=0
};

def macroop VEX_KMOVD_R_M {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_KMOVD_R_P {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_KMOVQ_K_K {
    gem5_moveto_opmask k, km, size=8, ext=1
};

def macroop VEX_KMOVQ_K_M {
    ldmask umask1, seg, sib, disp, dataSize=8
    gem5_moveto_opmask k, umask1, size=8, ext=1
};

def macroop VEX_KMOVQ_K_P {
    rdip t7
    ldmask umask1, seg, riprel, disp, dataSize=8
    gem5_moveto_opmask k, umask1, size=8, ext=1
};

def macroop VEX_KMOVQ_K_R {
    gem5_moveto_opmask k, regm, size=8, ext=0
};

def macroop VEX_KMOVQ_R_K {
    gem5_movefrom_opmask reg, km, size=8, ext=0
};

def macroop VEX_KMOVQ_R_M {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_KMOVQ_R_P {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VMOVD_XMM_R {
    gem5_mm256_move_epi32_si128 xmm, regm, srcSize=dsz, destSize=8
};

def macroop VEX_VMOVD_XMM_M {
    ldvec256lo64 xmm, seg, sib, disp, dataSize=dsz
};

def macroop VEX_VMOVD_XMM_P {
    rdip t7
    ldvec256lo64 xmm, seg, riprel, disp, dataSize=dsz
};

def macroop VEX_VMOVD_R_XMM {
    gem5_mm256_move_si128_epi32 reg, xmmm, size=dsz
};

def macroop VEX_VMOVD_M_XMM {
    stvec128lo xmm, seg, sib, disp, dataSize=dsz
};

def macroop VEX_VMOVD_P_XMM {
    rdip t7
    stvec128lo xmm, seg, riprel, disp, dataSize=dsz
};

def macroop VEX_VMOVQ_XMM_XMM {
    gem5_avx_move_epu64 xmm, xmmm, size=8, ext=Scalar
};

def macroop VEX_VMOVQ_XMM_R {
   gem5_mm256_move_epi64_si128 xmm, regm, srcSize=8, destSize=8
};

def macroop VEX_VMOVQ_XMM_M {
    ldvec256lo64 xmm, seg, sib, disp, dataSize=8
};

def macroop VEX_VMOVQ_XMM_P {
    rdip t7
    ldvec256lo64 xmm, seg, riprel, disp, dataSize=8
};

def macroop VEX_VMOVQ_R_XMM {
    gem5_mm256_move_si128_epi64 reg, xmmm, size=8
};

def macroop VEX_VMOVQ_M_XMM {
    stvec128lo xmm, seg, sib, disp, dataSize=8
};

def macroop VEX_VMOVQ_P_XMM {
    rdip t7
    stvec128lo xmm, seg, riprel, disp, dataSize=8
};

def macroop VEX_VMOVDQA_XMM_XMM {
    gem5_avx_move_epu64 xmm, xmmm, size=8, ext=XMM
};

def macroop VEX_VMOVDQA_XMM_M {
    ldvec128 xmm, seg, sib, disp, dataSize=16
};

def macroop VEX_VMOVDQA_XMM_P {
    rdip t7
    ldvec128 xmm, seg, riprel, disp, dataSize=16
};

def macroop VEX_VMOVDQA_M_XMM {
    stvec128 xmm, seg, sib, disp, dataSize=16
};

def macroop VEX_VMOVDQA_P_XMM {
    rdip t7
    stvec128 xmm, seg, riprel, disp, dataSize=16
};

def macroop VEX_VMOVDQA_YMM_YMM {
    gem5_avx_move_epu64 ymm, ymmm, size=8, ext=YMM
};

def macroop VEX_VMOVDQA_YMM_M {
    ldvec256 ymm, seg, sib, disp, dataSize=32
};

def macroop VEX_VMOVDQA_YMM_P {
    rdip t7
    ldvec256 ymm, seg, riprel, disp, dataSize=32
};

def macroop VEX_VMOVDQA_M_YMM {
    stvec256 ymm, seg, sib, disp, dataSize=32
};

def macroop VEX_VMOVDQA_P_YMM {
    rdip t7
    stvec256 ymm, seg, riprel, disp, dataSize=32
};

def macroop VEX_VMOVDQU_XMM_XMM {
    gem5_avx_move_epu64 xmm, xmmm, size=8, ext=XMM
};

def macroop VEX_VMOVDQU_XMM_M {
    ldvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop VEX_VMOVDQU_XMM_P {
    rdip t7
    ldvec128 xmm, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop VEX_VMOVDQU_M_XMM {
    stvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop VEX_VMOVDQU_P_XMM {
    rdip t7
    stvec128 xmm, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop VEX_VMOVDQU_YMM_YMM {
    gem5_avx_move_epu64 ymm, ymmm, size=8, ext=YMM
};

def macroop VEX_VMOVDQU_YMM_M {
    ldvec256 ymm, seg, sib, "DISPLACEMENT", dataSize=32
};

def macroop VEX_VMOVDQU_YMM_P {
    rdip t7
    ldvec256 ymm, seg, riprel, "DISPLACEMENT", dataSize=32
};

def macroop VEX_VMOVDQU_M_YMM {
    stvec256 ymm, seg, sib, "DISPLACEMENT", dataSize=32
};

def macroop VEX_VMOVDQU_P_YMM {
    rdip t7
    stvec256 ymm, seg, riprel, "DISPLACEMENT", dataSize=32
};
 
'''
