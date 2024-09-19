microcode = '''
def macroop VEX_VMOVSS_XMM_XMM {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VMOVSS_XMM_M {
    gem5_mm_load_ss xmm, seg, sib, disp, dataSize=4
};

def macroop VEX_VMOVSS_XMM_P {
    rdip t7
    gem5_mm_load_ss xmm, seg, riprel, disp, dataSize=4
};

def macroop VEX_VMOVSS_M_XMM {
    gem5_mm_store_ss xmm, seg, sib, disp, dataSize=4
};

def macroop VEX_VMOVSS_P_XMM {
    rdip t7
    gem5_mm_store_ss xmm, seg, riprel, disp, dataSize=4
};

def macroop VEX_VMOVSS_XMM_XMM_XMM {
    gem5_avx_move_ss xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop VEX_VMOVSS_XMM_XMM_M {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VMOVSS_XMM_XMM_P {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VMOVSS_M_XMM_XMM {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VMOVSS_P_XMM_XMM {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VMOVSD_XMM_XMM {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VMOVSD_XMM_M {
   ldvec128lo0 xmm, seg, sib, disp, dataSize=8
};

def macroop VEX_VMOVSD_XMM_P {
    rdip t7
    ldvec128lo0 xmm, seg, riprel, disp, dataSize=8
};

def macroop VEX_VMOVSD_M_XMM {
    stvec128lo xmm, seg, sib, disp, dataSize=8
};

def macroop VEX_VMOVSD_P_XMM {
    rdip t7
    stvec128lo xmm, seg, riprel, disp, dataSize=8
};

def macroop VEX_VMOVSD_XMM_XMM_XMM {
    gem5_avx_move_sd xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop VEX_VMOVSD_XMM_XMM_M {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VMOVSD_XMM_XMM_P {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VMOVSD_M_XMM_XMM {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VMOVSD_P_XMM_XMM {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VMOVAPS_XMM_XMM {
    # Check low address.
    gem5_avx_move_epu32 xmm, xmmm, size=4, ext=XMM
};

def macroop VEX_VMOVAPS_XMM_M {
    # Check low address.
    ldvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop VEX_VMOVAPS_XMM_P {
    rdip t7
    # Check low address.
    ldvec128 xmm, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop VEX_VMOVAPS_M_XMM {
    # Check low address.
    stvec128 xmm, seg, sib, disp, dataSize=16
};

def macroop VEX_VMOVAPS_P_XMM {
    rdip t7
    # Check low address.
    stvec128 xmm, seg, riprel, disp, dataSize=16
};

def macroop VEX_VMOVAPS_YMM_YMM {
    # Check low address.
    gem5_avx_move_epu32 ymm, ymmm, size=4, ext=YMM
};

def macroop VEX_VMOVAPS_YMM_M {
    # Check low address.
    ldvec256 ymm, seg, sib, disp, dataSize=32
};

def macroop VEX_VMOVAPS_YMM_P {
    rdip t7
    # Check low address.
    ldvec256 ymm, seg, riprel, disp, dataSize=32
};

def macroop VEX_VMOVAPS_M_YMM {
    # Check low address.
    stvec256 ymm, seg, sib, disp, dataSize=32
};

def macroop VEX_VMOVAPS_P_YMM {
    rdip t7
    # Check low address.
    stvec256 ymm, seg, riprel, disp, dataSize=32
};

def macroop VEX_VMOVAPD_XMM_XMM {
    # Check low address.
    gem5_avx_move_epu64 xmm, xmmm, size=8, ext=XMM
};

def macroop VEX_VMOVAPD_XMM_M {
    # Check low address.
    ldvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop VEX_VMOVAPD_XMM_P {
    rdip t7
    # Check low address.
    ldvec128 xmm, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop VEX_VMOVAPD_M_XMM {
    # Check low address.
    stvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop VEX_VMOVAPD_P_XMM {
    rdip t7
    # Check low address.
    stvec128 xmm, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop VEX_VMOVAPD_YMM_YMM {
    # Check low address.
    gem5_avx_move_epu64 ymm, ymmm, size=8, ext=YMM
};

def macroop VEX_VMOVAPD_YMM_M {
    # Check low address.
    ldvec256 ymm, seg, sib, "DISPLACEMENT", dataSize=32
};

def macroop VEX_VMOVAPD_YMM_P {
    rdip t7
    # Check low address.
    ldvec256 ymm, seg, riprel, "DISPLACEMENT", dataSize=32
};

def macroop VEX_VMOVAPD_M_YMM {
    # Check low address.
    stvec256 ymm, seg, sib, "DISPLACEMENT", dataSize=32
};

def macroop VEX_VMOVAPD_P_YMM {
    rdip t7
    # Check low address.
    stvec256 ymm, seg, riprel, "DISPLACEMENT", dataSize=32
};

def macroop VEX_VMOVUPS_XMM_XMM {
    gem5_avx_move_epu32 xmm, xmmm, size=4, ext=XMM
};

def macroop VEX_VMOVUPS_XMM_M {
    ldvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop VEX_VMOVUPS_XMM_P {
    rdip t7
    ldvec128 xmm, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop VEX_VMOVUPS_M_XMM {
    stvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop VEX_VMOVUPS_P_XMM {
    rdip t7
    stvec128 xmm, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop VEX_VMOVUPS_YMM_YMM {
    gem5_avx_move_epu32 ymm, ymmm, size=4, ext=YMM
};

def macroop VEX_VMOVUPS_YMM_M {
    ldvec256 ymm, seg, sib, "DISPLACEMENT", dataSize=32
};

def macroop VEX_VMOVUPS_YMM_P {
    rdip t7
    ldvec256 ymm, seg, riprel, "DISPLACEMENT", dataSize=32
};

def macroop VEX_VMOVUPS_M_YMM {
    stvec256 ymm, seg, sib, "DISPLACEMENT", dataSize=32
};

def macroop VEX_VMOVUPS_P_YMM {
    rdip t7
    stvec256 ymm, seg, riprel, "DISPLACEMENT", dataSize=32
};

def macroop VEX_VMOVUPD_XMM_XMM {
    gem5_avx_move_epu64 xmm, xmmm, size=8, ext=XMM
};

def macroop VEX_VMOVUPD_XMM_M {
    ldvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop VEX_VMOVUPD_XMM_P {
    rdip t7
    ldvec128 xmm, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop VEX_VMOVUPD_M_XMM {
    stvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop VEX_VMOVUPD_P_XMM {
    rdip t7
    stvec128 xmm, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop VEX_VMOVUPD_YMM_YMM {
    gem5_avx_move_epu64 ymm, ymmm, size=8, ext=YMM
};

def macroop VEX_VMOVUPD_YMM_M {
    ldvec256 ymm, seg, sib, "DISPLACEMENT", dataSize=32
};

def macroop VEX_VMOVUPD_YMM_P {
    rdip t7
    ldvec256 ymm, seg, riprel, "DISPLACEMENT", dataSize=32
};

def macroop VEX_VMOVUPD_M_YMM {
    stvec256 ymm, seg, sib, "DISPLACEMENT", dataSize=32
};

def macroop VEX_VMOVUPD_P_YMM {
    rdip t7
    stvec256 ymm, seg, riprel, "DISPLACEMENT", dataSize=32
};

def macroop VEX_VMOVHPD_XMM_XMM_M {
    ldvec128lo0 uvec1, seg, sib, "DISPLACEMENT", dataSize=8
    gem5_avx_unpacklo_epu64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VMOVHPD_XMM_XMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_unpacklo_epu64 xmm1, xmm2, uvec1, size=8, ext=XMM
};

def macroop VEX_VMOVHPD_M_XMM {
    stvec128hi xmm, seg, sib, disp, dataSize=8
};

def macroop VEX_VMOVHPD_P_XMM {
    rdip t7
    stvec128hi xmm, seg, riprel, disp, dataSize=8
};

def macroop VEX_VMOVLPS_XMM_XMM_M {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    gem5_avx_loadl_pi xmm1, xmm2, uvec1, size=8
};

def macroop VEX_VMOVLPS_XMM_XMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_loadl_pi xmm1, xmm2, uvec1, size=8
};

def macroop VEX_VMOVLPS_M_XMM {
    stvec128lo xmm, seg, sib, disp, dataSize=8
};

def macroop VEX_VMOVLPS_P_XMM {
    rdip t7
    stvec128lo xmm, seg, riprel, disp, dataSize=8
};

def macroop VEX_VMOVLPD_XMM_XMM_M {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    gem5_avx_loadl_pi xmm1, xmm2, uvec1, size=8
};

def macroop VEX_VMOVLPD_XMM_XMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_loadl_pi xmm1, xmm2, uvec1, size=8
};

def macroop VEX_VMOVLPD_M_XMM {
    stvec128lo xmm, seg, sib, disp, dataSize=8
};

def macroop VEX_VMOVLPD_P_XMM {
    rdip t7
    stvec128lo xmm, seg, riprel, disp, dataSize=8
};

def macroop VEX_VMOVHPS_XMM_XMM_XMM {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VMOVHPS_XMM_XMM_M {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    gem5_avx_loadh_pi xmm1, xmm2, uvec1, size=8
};

def macroop VEX_VMOVHPS_XMM_XMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_loadh_pi xmm1, xmm2, uvec1, size=8
};

def macroop VEX_VMOVHPS_M_XMM {
    stvec128hi xmm, seg, sib, disp, dataSize=8
};

def macroop VEX_VMOVHPS_P_XMM {
    rdip t7
    stvec128hi xmm, seg, riprel, disp, dataSize=8
};

def macroop VEX_VMOVHPD_XMM_XMM_M {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    gem5_avx_loadh_pi xmm1, xmm2, uvec1, size=8
};

def macroop VEX_VMOVHPD_XMM_XMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_loadh_pi xmm1, xmm2, uvec1, size=8
};

def macroop VEX_VMOVHPD_M_XMM {
    stvec128hi xmm, seg, sib, disp, dataSize=8
};

def macroop VEX_VMOVHPD_P_XMM {
    rdip t7
    stvec128hi xmm, seg, riprel, disp, dataSize=8
};

def macroop VEX_VMOVHLPS_XMM_XMM_XMM {
    gem5_avx_unpackhi_epu64 xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop VEX_VMOVHLPS_XMM_XMM_M {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VMOVHLPS_XMM_XMM_P {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VMOVLHPS_XMM_XMM_XMM {
    gem5_avx_unpacklo_epu64 xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop VEX_VMOVLHPS_XMM_XMM_M {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop VEX_VMOVLHPS_XMM_XMM_P {
    fault "std::make_shared<UnimpInstFault>()"
};

'''
