microcode = '''
def macroop EVEX_VMOVSS_XMM_XMM {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VMOVSS_XMM_M {
    gem5_mm_load_ss xmm, seg, sib, disp, dataSize=4
};

def macroop EVEX_VMOVSS_XMM_P {
    rdip t7
    gem5_mm_load_ss xmm, seg, riprel, disp, dataSize=4
};

def macroop EVEX_VMOVSS_M_XMM {
    gem5_mm_store_ss xmm, seg, sib, disp, dataSize=4
};

def macroop EVEX_VMOVSS_P_XMM {
    rdip t7
    gem5_mm_store_ss xmm, seg, riprel, disp, dataSize=4
};

def macroop EVEX_VMOVSS_XMM_XMM_XMM {
    gem5_avx_move_ss xmm1, xmm2, xmmm, size=4, ext=XMM
};

def macroop EVEX_VMOVSS_XMM_XMM_M {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VMOVSS_XMM_XMM_P {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VMOVSS_M_XMM_XMM {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VMOVSS_P_XMM_XMM {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VMOVSD_XMM_XMM {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VMOVSD_XMM_M {
   ldvec128lo0 xmm, seg, sib, disp, dataSize=8
};

def macroop EVEX_VMOVSD_XMM_P {
    rdip t7
    ldvec128lo0 xmm, seg, riprel, disp, dataSize=8
};

def macroop EVEX_VMOVSD_M_XMM {
    stvec128lo xmm, seg, sib, disp, dataSize=8
};

def macroop EVEX_VMOVSD_P_XMM {
    rdip t7
    stvec128lo xmm, seg, riprel, disp, dataSize=8
};

def macroop EVEX_VMOVSD_XMM_XMM_XMM {
    gem5_avx_move_sd xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop EVEX_VMOVSD_XMM_XMM_M {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VMOVSD_XMM_XMM_P {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VMOVSD_M_XMM_XMM {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VMOVSD_P_XMM_XMM {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VMOVAPS_XMM_XMM {
    # Check low address.
    gem5_avx_move_epu32 xmm, xmmm, size=4, ext=XMM
};

def macroop EVEX_VMOVAPS_XMM_M {
    # Check low address.
    ldvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVAPS_XMM_P {
    rdip t7
    # Check low address.
    ldvec128 xmm, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVAPSR_XMM_XMM {
    # Check low address.
    gem5_avx_move_epu32 xmmm, xmm, size=4, ext=XMM
};

def macroop EVEX_VMOVAPSR_M_XMM {
    # Check low address.
    stvec128 xmm, seg, sib, disp, dataSize=16
};

def macroop EVEX_VMOVAPSR_P_XMM {
    rdip t7
    # Check low address.
    stvec128 xmm, seg, riprel, disp, dataSize=16
};

def macroop EVEX_VMOVAPS_YMM_YMM {
    # Check low address.
    gem5_avx_move_epu32 ymm, ymmm, size=4, ext=YMM
};

def macroop EVEX_VMOVAPS_YMM_M {
    # Check low address.
    ldvec256 ymm, seg, sib, disp, dataSize=32
};

def macroop EVEX_VMOVAPS_YMM_P {
    rdip t7
    # Check low address.
    ldvec256 ymm, seg, riprel, disp, dataSize=32
};

def macroop EVEX_VMOVAPSR_YMM_YMM {
    # Check low address.
    gem5_avx_move_epu32 ymmm, ymm, size=4, ext=YMM
};

def macroop EVEX_VMOVAPSR_M_YMM {
    # Check low address.
    stvec256 ymm, seg, sib, disp, dataSize=32
};

def macroop EVEX_VMOVAPSR_P_YMM {
    rdip t7
    # Check low address.
    stvec256 ymm, seg, riprel, disp, dataSize=32
};

def macroop EVEX_VMOVAPS_ZMM_ZMM {
    # Check low address.
    gem5_avx_move_epu32 zmm, zmmm, size=4, ext=ZMM
};

def macroop EVEX_VMOVAPS_ZMM_M {
    # Check low address.
    ldvec512 zmm, seg, sib, disp, dataSize=64
};

def macroop EVEX_VMOVAPS_ZMM_P {
    rdip t7
    # Check low address.
    ldvec512 zmm, seg, riprel, disp, dataSize=64
};

def macroop EVEX_VMOVAPSR_ZMM_ZMM {
    # Check low address.
    gem5_avx_move_epu32 zmmm, zmm, size=4, ext=ZMM
};

def macroop EVEX_VMOVAPSR_M_ZMM {
    # Check low address.
    stvec512 zmm, seg, sib, disp, dataSize=64
};

def macroop EVEX_VMOVAPSR_P_ZMM {
    rdip t7
    stvec512 zmm, seg, riprel, disp, dataSize=64
};

def macroop EVEX_VMOVAPD_XMM_XMM {
    gem5_avx_move_epu64 xmm, xmmm, size=8, ext=XMM
};

def macroop EVEX_VMOVAPD_XMM_M {
    ldvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVAPD_XMM_P {
    rdip t7
    ldvec128 xmm, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVAPDR_XMM_XMM {
    gem5_avx_move_epu64 xmmm, xmm, size=8, ext=XMM
};

def macroop EVEX_VMOVAPDR_M_XMM {
    stvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVAPDR_P_XMM {
    rdip t7
    stvec128 xmm, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVAPD_YMM_YMM {
    gem5_avx_move_epu64 ymm, ymmm, size=8, ext=YMM
};

def macroop EVEX_VMOVAPD_YMM_M {
    ldvec256 ymm, seg, sib, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVAPD_YMM_P {
    rdip t7
    ldvec256 ymm, seg, riprel, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVAPDR_YMM_YMM {
    gem5_avx_move_epu64 ymmm, ymm, size=8, ext=YMM
};

def macroop EVEX_VMOVAPDR_M_YMM {
    stvec256 ymm, seg, sib, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVAPDR_P_YMM {
    rdip t7
    stvec256 ymm, seg, riprel, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVAPD_ZMM_ZMM {
    gem5_avx_move_epu64 zmm, zmmm, size=8, ext=ZMM
};

def macroop EVEX_VMOVAPD_ZMM_M {
    ldvec512 zmm, seg, sib, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVAPD_ZMM_P {
    rdip t7
    ldvec512 zmm, seg, riprel, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVAPDR_ZMM_ZMM {
    gem5_avx_move_epu64 zmmm, zmm, size=8, ext=ZMM
};

def macroop EVEX_VMOVAPDR_M_ZMM {
    stvec512 zmm, seg, sib, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVAPDR_P_ZMM {
    rdip t7
    stvec512 zmm, seg, riprel, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVUPS_XMM_XMM {
    gem5_avx_move_epu32 xmm, xmmm, size=4, ext=XMM
};

def macroop EVEX_VMOVUPS_XMM_M {
    ldvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVUPS_XMM_P {
    rdip t7
    ldvec128 xmm, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVUPSR_XMM_XMM {
    gem5_avx_move_epu32 xmmm, xmm, size=4, ext=XMM
};

def macroop EVEX_VMOVUPSR_M_XMM {
    stvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVUPSR_P_XMM {
    rdip t7
    stvec128 xmm, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVUPS_YMM_YMM {
    gem5_avx_move_epu32 ymm, ymmm, size=4, ext=YMM
};

def macroop EVEX_VMOVUPS_YMM_M {
    ldvec256 ymm, seg, sib, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVUPS_YMM_P {
    rdip t7
    ldvec256 ymm, seg, riprel, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVUPSR_YMM_YMM {
    gem5_avx_move_epu32 ymmm, ymm, size=4, ext=YMM
};

def macroop EVEX_VMOVUPSR_M_YMM {
    stvec256 ymm, seg, sib, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVUPSR_P_YMM {
    rdip t7
    stvec256 ymm, seg, riprel, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVUPS_ZMM_ZMM {
    gem5_avx_move_epu32 zmm, zmmm, size=4, ext=ZMM
};

def macroop EVEX_VMOVUPS_ZMM_M {
    ldvec512 zmm, seg, sib, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVUPS_ZMM_P {
    rdip t7
    ldvec512 zmm, seg, riprel, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVUPSR_ZMM_ZMM {
    gem5_avx_move_epu32 zmmm, zmm, size=4, ext=ZMM
};

def macroop EVEX_VMOVUPSR_M_ZMM {
    stvec512 zmm, seg, sib, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVUPSR_P_ZMM {
    rdip t7
    stvec512 zmm, seg, riprel, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVUPD_XMM_XMM {
    gem5_avx_move_epu64 xmm, xmmm, size=8, ext=XMM
};

def macroop EVEX_VMOVUPD_XMM_M {
    ldvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVUPD_XMM_P {
    rdip t7
    ldvec128 xmm, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVUPDR_XMM_XMM {
    gem5_avx_move_epu64 xmmm, xmm, size=8, ext=XMM
};

def macroop EVEX_VMOVUPDR_M_XMM {
    stvec128 xmm, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVUPDR_P_XMM {
    rdip t7
    stvec128 xmm, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVUPD_YMM_YMM {
    gem5_avx_move_epu64 ymm, ymmm, size=8, ext=YMM
};

def macroop EVEX_VMOVUPD_YMM_M {
    ldvec256 ymm, seg, sib, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVUPD_YMM_P {
    rdip t7
    ldvec256 ymm, seg, riprel, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVUPDR_YMM_YMM {
    gem5_avx_move_epu64 ymmm, ymm, size=8, ext=YMM
};

def macroop EVEX_VMOVUPDR_M_YMM {
    stvec256 ymm, seg, sib, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVUPDR_P_YMM {
    rdip t7
    stvec256 ymm, seg, riprel, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVUPD_ZMM_ZMM {
    gem5_avx_move_epu64 zmm, zmmm, size=8, ext=ZMM
};

def macroop EVEX_VMOVUPD_ZMM_M {
    ldvec512 zmm, seg, sib, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVUPD_ZMM_P {
    rdip t7
    ldvec512 zmm, seg, riprel, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVUPDR_ZMM_ZMM {
    gem5_avx_move_epu64 zmm, zmmm, size=8, ext=ZMM
};

def macroop EVEX_VMOVUPDR_M_ZMM {
    stvec512 zmm, seg, sib, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVUPDR_P_ZMM {
    rdip t7
    stvec512 zmm, seg, riprel, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVLPS_XMM_XMM_M {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    gem5_avx_loadl_pi xmm1, xmm2, uvec1, size=8
};

def macroop EVEX_VMOVLPS_XMM_XMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_loadl_pi xmm1, xmm2, uvec1, size=8
};

def macroop EVEX_VMOVLPS_M_XMM {
    stvec128lo xmm, seg, sib, disp, dataSize=8
};

def macroop EVEX_VMOVLPS_P_XMM {
    rdip t7
    stvec128lo xmm, seg, riprel, disp, dataSize=8
};

def macroop EVEX_VMOVLPD_XMM_XMM_M {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    gem5_avx_loadl_pi xmm1, xmm2, uvec1, size=8
};

def macroop EVEX_VMOVLPD_XMM_XMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_loadl_pi xmm1, xmm2, uvec1, size=8
};

def macroop EVEX_VMOVLPD_M_XMM {
    stvec128lo xmm, seg, sib, disp, dataSize=8
};

def macroop EVEX_VMOVLPD_P_XMM {
    rdip t7
    stvec128lo xmm, seg, riprel, disp, dataSize=8
};

def macroop EVEX_VMOVHPS_XMM_XMM_XMM {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VMOVHPS_XMM_XMM_M {
    ldvec128lo0 uvec1, seg, sib, disp, dataSize=8
    gem5_avx_loadh_pi xmm1, xmm2, uvec1, size=8
};

def macroop EVEX_VMOVHPS_XMM_XMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_loadh_pi xmm1, xmm2, uvec1, size=8
};

def macroop EVEX_VMOVHPS_M_XMM {
    stvec128hi xmm, seg, sib, disp, dataSize=8
};

def macroop EVEX_VMOVHPS_P_XMM {
    rdip t7
    stvec128hi xmm, seg, riprel, disp, dataSize=8
};

def macroop EVEX_VMOVHPD_XMM_XMM_M {
    ldvec128lo0 uvec1, seg, sib, "DISPLACEMENT", dataSize=8
    gem5_avx_unpacklo_epu64 xmm1, xmm2, src2=uvec1, size=8, ext=XMM
};

def macroop EVEX_VMOVHPD_XMM_XMM_P {
    rdip t7
    ldvec128lo0 uvec1, seg, riprel, disp, dataSize=8
    gem5_avx_unpacklo_epu64 xmm1, xmm2, src2=uvec1, size=8, ext=XMM
};

def macroop EVEX_VMOVHPD_M_XMM {
    stvec128hi xmm, seg, sib, disp, dataSize=8
};

def macroop EVEX_VMOVHPD_P_XMM {
    rdip t7
    stvec128hi xmm, seg, riprel, disp, dataSize=8
};

def macroop EVEX_VMOVHLPS_XMM_XMM_XMM {
    gem5_avx_unpackhi_epu64 xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop EVEX_VMOVHLPS_XMM_XMM_M {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VMOVHLPS_XMM_XMM_P {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VMOVLHPS_XMM_XMM_XMM {
    gem5_avx_unpacklo_epu64 xmm1, xmm2, xmmm, size=8, ext=XMM
};

def macroop EVEX_VMOVLHPS_XMM_XMM_M {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VMOVLHPS_XMM_XMM_P {
    fault "std::make_shared<UnimpInstFault>()"
};

def macroop EVEX_VMOVUPS_XMM_XMM_K {
    gem5_mask_move_epu32 xmm, xmmm, opmask=opmask, src2=xmm, size=4, ext=XMM
};

def macroop EVEX_VMOVUPS_XMM_M_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_move_epu32 xmm, uvec1, opmask=opmask, src2=xmm, size=4, ext=XMM
};

def macroop EVEX_VMOVUPS_XMM_P_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_move_epu32 xmm, uvec1, opmask=opmask, src2=xmm, size=4, ext=XMM
};

def macroop EVEX_VMOVUPS_M_XMM_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_move_epu32 uvec1, xmm, opmask=opmask, src2=uvec1, size=4, ext=XMM
    stvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVUPS_P_XMM_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_move_epu32 uvec1, xmm, opmask=opmask, src2=uvec1, size=4, ext=XMM
    stvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVUPS_YMM_YMM_K {
    gem5_mask_move_epu32 ymm, ymmm, opmask=opmask, src2=ymm, size=4, ext=YMM
};

def macroop EVEX_VMOVUPS_YMM_M_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_move_epu32 ymm, uvec1, opmask=opmask, src2=ymm, size=4, ext=YMM
};

def macroop EVEX_VMOVUPS_YMM_P_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_move_epu32 ymm, uvec1, opmask=opmask, src2=ymm, size=4, ext=YMM
};

def macroop EVEX_VMOVUPS_M_YMM_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_move_epu32 uvec1, ymm, opmask=opmask, src2=uvec1, size=4, ext=YMM
    stvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVUPS_P_YMM_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_move_epu32 uvec1, ymm, opmask=opmask, src2=uvec1, size=4, ext=YMM
    stvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVUPS_ZMM_ZMM_K {
    gem5_mask_move_epu32 zmm, zmmm, opmask=opmask, src2=zmm, size=4, ext=ZMM
};

def macroop EVEX_VMOVUPS_ZMM_M_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_move_epu32 zmm, uvec1, opmask=opmask, src2=zmm, size=4, ext=ZMM
};

def macroop EVEX_VMOVUPS_ZMM_P_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_move_epu32 zmm, uvec1, opmask=opmask, src2=zmm, size=4, ext=ZMM
};

def macroop EVEX_VMOVUPS_M_ZMM_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_move_epu32 uvec1, zmm, opmask=opmask, src2=uvec1, size=4, ext=ZMM
    stvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVUPS_P_ZMM_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_move_epu32 uvec1, zmm, opmask=opmask, src2=uvec1, size=4, ext=ZMM
    stvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVUPD_XMM_XMM_K {
    gem5_mask_move_epu64 xmm, xmmm, opmask=opmask, src2=xmm, size=8, ext=XMM
};

def macroop EVEX_VMOVUPD_XMM_M_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_move_epu64 xmm, uvec1, opmask=opmask, src2=xmm, size=8, ext=XMM
};

def macroop EVEX_VMOVUPD_XMM_P_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_move_epu64 xmm, uvec1, opmask=opmask, src2=xmm, size=8, ext=XMM
};

def macroop EVEX_VMOVUPD_M_XMM_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_move_epu64 uvec1, xmm, opmask=opmask, src2=uvec1, size=8, ext=XMM
    stvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVUPD_P_XMM_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_move_epu64 uvec1, xmm, opmask=opmask, src2=uvec1, size=8, ext=XMM
    stvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVUPD_YMM_YMM_K {
    gem5_mask_move_epu64 ymm, ymmm, opmask=opmask, src2=ymm, size=8, ext=YMM
};

def macroop EVEX_VMOVUPD_YMM_M_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_move_epu64 ymm, uvec1, opmask=opmask, src2=ymm, size=8, ext=YMM
};

def macroop EVEX_VMOVUPD_YMM_P_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_move_epu64 ymm, uvec1, opmask=opmask, src2=ymm, size=8, ext=YMM
};

def macroop EVEX_VMOVUPD_M_YMM_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_move_epu64 uvec1, ymm, opmask=opmask, src2=uvec1, size=8, ext=YMM
    stvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVUPD_P_YMM_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_move_epu64 uvec1, ymm, opmask=opmask, src2=uvec1, size=8, ext=YMM
    stvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVUPD_ZMM_ZMM_K {
    gem5_mask_move_epu64 zmm, zmmm, opmask=opmask, src2=zmm, size=8, ext=ZMM
};

def macroop EVEX_VMOVUPD_ZMM_M_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_move_epu64 zmm, uvec1, opmask=opmask, src2=zmm, size=8, ext=ZMM
};

def macroop EVEX_VMOVUPD_ZMM_P_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_move_epu64 zmm, uvec1, opmask=opmask, src2=zmm, size=8, ext=ZMM
};

def macroop EVEX_VMOVUPD_M_ZMM_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_move_epu64 uvec1, zmm, opmask=opmask, src2=uvec1, size=8, ext=ZMM
    stvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVUPD_P_ZMM_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_move_epu64 uvec1, zmm, opmask=opmask, src2=uvec1, size=8, ext=ZMM
    stvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVAPS_XMM_XMM_K {
    gem5_mask_move_epu32 xmm, xmmm, opmask=opmask, src2=xmm, size=4, ext=XMM
};

def macroop EVEX_VMOVAPS_XMM_M_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_move_epu32 xmm, uvec1, opmask=opmask, src2=xmm, size=4, ext=XMM
};

def macroop EVEX_VMOVAPS_XMM_P_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_move_epu32 xmm, uvec1, opmask=opmask, src2=xmm, size=4, ext=XMM
};

def macroop EVEX_VMOVAPS_M_XMM_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_move_epu32 uvec1, xmm, opmask=opmask, src2=uvec1, size=4, ext=XMM
    stvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVAPS_P_XMM_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_move_epu32 uvec1, xmm, opmask=opmask, src2=uvec1, size=4, ext=XMM
    stvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVAPS_YMM_YMM_K {
    gem5_mask_move_epu32 ymm, ymmm, opmask=opmask, src2=ymm, size=4, ext=YMM
};

def macroop EVEX_VMOVAPS_YMM_M_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_move_epu32 ymm, uvec1, opmask=opmask, src2=ymm, size=4, ext=YMM
};

def macroop EVEX_VMOVAPS_YMM_P_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_move_epu32 ymm, uvec1, opmask=opmask, src2=ymm, size=4, ext=YMM
};

def macroop EVEX_VMOVAPS_M_YMM_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_move_epu32 uvec1, ymm, opmask=opmask, src2=uvec1, size=4, ext=YMM
    stvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVAPS_P_YMM_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_move_epu32 uvec1, ymm, opmask=opmask, src2=uvec1, size=4, ext=YMM
    stvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVAPS_ZMM_ZMM_K {
    gem5_mask_move_epu32 zmm, zmmm, opmask=opmask, src2=zmm, size=4, ext=ZMM
};

def macroop EVEX_VMOVAPS_ZMM_M_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_move_epu32 zmm, uvec1, opmask=opmask, src2=zmm, size=4, ext=ZMM
};

def macroop EVEX_VMOVAPS_ZMM_P_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_move_epu32 zmm, uvec1, opmask=opmask, src2=zmm, size=4, ext=ZMM
};

def macroop EVEX_VMOVAPS_M_ZMM_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_move_epu32 uvec1, zmm, opmask=opmask, src2=uvec1, size=4, ext=ZMM
    stvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVAPS_P_ZMM_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_move_epu32 uvec1, zmm, opmask=opmask, src2=uvec1, size=4, ext=ZMM
    stvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVAPD_XMM_XMM_K {
    gem5_mask_move_epu64 xmm, xmmm, opmask=opmask, src2=xmm, size=8, ext=XMM
};

def macroop EVEX_VMOVAPD_XMM_M_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_move_epu64 xmm, uvec1, opmask=opmask, src2=xmm, size=8, ext=XMM
};

def macroop EVEX_VMOVAPD_XMM_P_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_move_epu64 xmm, uvec1, opmask=opmask, src2=xmm, size=8, ext=XMM
};

def macroop EVEX_VMOVAPD_M_XMM_K {
    ldvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
    gem5_mask_move_epu64 uvec1, xmm, opmask=opmask, src2=uvec1, size=8, ext=XMM
    stvec128 uvec1, seg, sib, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVAPD_P_XMM_K {
    rdip t7
    ldvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
    gem5_mask_move_epu64 uvec1, xmm, opmask=opmask, src2=uvec1, size=8, ext=XMM
    stvec128 uvec1, seg, riprel, "DISPLACEMENT", dataSize=16
};

def macroop EVEX_VMOVAPD_YMM_YMM_K {
    gem5_mask_move_epu64 ymm, ymmm, opmask=opmask, src2=ymm, size=8, ext=YMM
};

def macroop EVEX_VMOVAPD_YMM_M_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_move_epu64 ymm, uvec1, opmask=opmask, src2=ymm, size=8, ext=YMM
};

def macroop EVEX_VMOVAPD_YMM_P_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_move_epu64 ymm, uvec1, opmask=opmask, src2=ymm, size=8, ext=YMM
};

def macroop EVEX_VMOVAPD_M_YMM_K {
    ldvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
    gem5_mask_move_epu64 uvec1, ymm, opmask=opmask, src2=uvec1, size=8, ext=YMM
    stvec256 uvec1, seg, sib, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVAPD_P_YMM_K {
    rdip t7
    ldvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
    gem5_mask_move_epu64 uvec1, ymm, opmask=opmask, src2=uvec1, size=8, ext=YMM
    stvec256 uvec1, seg, riprel, "DISPLACEMENT", dataSize=32
};

def macroop EVEX_VMOVAPD_ZMM_ZMM_K {
    gem5_mask_move_epu64 zmm, zmmm, opmask=opmask, src2=zmm, size=8, ext=ZMM
};

def macroop EVEX_VMOVAPD_ZMM_M_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_move_epu64 zmm, uvec1, opmask=opmask, src2=zmm, size=8, ext=ZMM
};

def macroop EVEX_VMOVAPD_ZMM_P_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_move_epu64 zmm, uvec1, opmask=opmask, src2=zmm, size=8, ext=ZMM
};

def macroop EVEX_VMOVAPD_M_ZMM_K {
    ldvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
    gem5_mask_move_epu64 uvec1, zmm, opmask=opmask, src2=uvec1, size=8, ext=ZMM
    stvec512 uvec1, seg, sib, "DISPLACEMENT", dataSize=64
};

def macroop EVEX_VMOVAPD_P_ZMM_K {
    rdip t7
    ldvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
    gem5_mask_move_epu64 uvec1, zmm, opmask=opmask, src2=uvec1, size=8, ext=ZMM
    stvec512 uvec1, seg, riprel, "DISPLACEMENT", dataSize=64
};

'''
