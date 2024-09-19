/*
 * Copyright (c) 2007 The Hewlett-Packard Development Company
 * All rights reserved.
 *
 * The license below extends only to copyright in the software and shall
 * not be construed as granting a license to any other intellectual
 * property including but not limited to intellectual property relating
 * to a hardware implementation of the functionality of the software
 * licensed hereunder.  You may use the software subject to the license
 * terms below provided that you ensure that this notice is replicated
 * unmodified and in its entirety in all distributions of the software,
 * modified or unmodified, in source code or in binary form.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are
 * met: redistributions of source code must retain the above copyright
 * notice, this list of conditions and the following disclaimer;
 * redistributions in binary form must reproduce the above copyright
 * notice, this list of conditions and the following disclaimer in the
 * documentation and/or other materials provided with the distribution;
 * neither the name of the copyright holders nor the names of its
 * contributors may be used to endorse or promote products derived from
 * this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 * A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
 * OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 * LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 * DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 * THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *
 * Authors: Gabe Black
 */

#ifndef __ARCH_X86_VECTORREGS_HH__
#define __ARCH_X86_VECTORREGS_HH__

#include "arch/x86/x86_traits.hh"
#include "base/bitunion.hh"

namespace X86ISA
{
    enum VectorRegIndex
    {
        // XMM registers
        VECTORREG_XMM_BASE,
        VECTORREG_XMM0_BASE = VECTORREG_XMM_BASE,
        VECTORREG_XMM1_BASE,
        VECTORREG_XMM2_BASE,
        VECTORREG_XMM3_BASE,
        VECTORREG_XMM4_BASE,
        VECTORREG_XMM5_BASE,
        VECTORREG_XMM6_BASE,
        VECTORREG_XMM7_BASE,
        VECTORREG_XMM8_BASE,
        VECTORREG_XMM9_BASE,
        VECTORREG_XMM10_BASE,
        VECTORREG_XMM11_BASE,
        VECTORREG_XMM12_BASE,
        VECTORREG_XMM13_BASE,
        VECTORREG_XMM14_BASE,
        VECTORREG_XMM15_BASE,
        VECTORREG_XMM16_BASE,
        VECTORREG_XMM17_BASE,
        VECTORREG_XMM18_BASE,
        VECTORREG_XMM19_BASE,
        VECTORREG_XMM20_BASE,
        VECTORREG_XMM21_BASE,
        VECTORREG_XMM22_BASE,
        VECTORREG_XMM23_BASE,
        VECTORREG_XMM24_BASE,
        VECTORREG_XMM25_BASE,
        VECTORREG_XMM26_BASE,
        VECTORREG_XMM27_BASE,
        VECTORREG_XMM28_BASE,
        VECTORREG_XMM29_BASE,
        VECTORREG_XMM30_BASE,
        VECTORREG_XMM31_BASE,

        // YMM registers
        VECTORREG_YMM_BASE  = VECTORREG_XMM_BASE,
        VECTORREG_YMM0_BASE = VECTORREG_YMM_BASE,
        VECTORREG_YMM1_BASE,
        VECTORREG_YMM2_BASE,
        VECTORREG_YMM3_BASE,
        VECTORREG_YMM4_BASE,
        VECTORREG_YMM5_BASE,
        VECTORREG_YMM6_BASE,
        VECTORREG_YMM7_BASE,
        VECTORREG_YMM8_BASE,
        VECTORREG_YMM9_BASE,
        VECTORREG_YMM10_BASE,
        VECTORREG_YMM11_BASE,
        VECTORREG_YMM12_BASE,
        VECTORREG_YMM13_BASE,
        VECTORREG_YMM14_BASE,
        VECTORREG_YMM15_BASE,
        VECTORREG_YMM16_BASE,
        VECTORREG_YMM17_BASE,
        VECTORREG_YMM18_BASE,
        VECTORREG_YMM19_BASE,
        VECTORREG_YMM20_BASE,
        VECTORREG_YMM21_BASE,
        VECTORREG_YMM22_BASE,
        VECTORREG_YMM23_BASE,
        VECTORREG_YMM24_BASE,
        VECTORREG_YMM25_BASE,
        VECTORREG_YMM26_BASE,
        VECTORREG_YMM27_BASE,
        VECTORREG_YMM28_BASE,
        VECTORREG_YMM29_BASE,
        VECTORREG_YMM30_BASE,
        VECTORREG_YMM31_BASE,

        // ZMM registers
        VECTORREG_ZMM_BASE  = VECTORREG_XMM_BASE,
        VECTORREG_ZMM0_BASE = VECTORREG_ZMM_BASE,
        VECTORREG_ZMM1_BASE,
        VECTORREG_ZMM2_BASE,
        VECTORREG_ZMM3_BASE,
        VECTORREG_ZMM4_BASE,
        VECTORREG_ZMM5_BASE,
        VECTORREG_ZMM6_BASE,
        VECTORREG_ZMM7_BASE,
        VECTORREG_ZMM8_BASE,
        VECTORREG_ZMM9_BASE,
        VECTORREG_ZMM10_BASE,
        VECTORREG_ZMM11_BASE,
        VECTORREG_ZMM12_BASE,
        VECTORREG_ZMM13_BASE,
        VECTORREG_ZMM14_BASE,
        VECTORREG_ZMM15_BASE,
        VECTORREG_ZMM16_BASE,
        VECTORREG_ZMM17_BASE,
        VECTORREG_ZMM18_BASE,
        VECTORREG_ZMM19_BASE,
        VECTORREG_ZMM20_BASE,
        VECTORREG_ZMM21_BASE,
        VECTORREG_ZMM22_BASE,
        VECTORREG_ZMM23_BASE,
        VECTORREG_ZMM24_BASE,
        VECTORREG_ZMM25_BASE,
        VECTORREG_ZMM26_BASE,
        VECTORREG_ZMM27_BASE,
        VECTORREG_ZMM28_BASE,
        VECTORREG_ZMM29_BASE,
        VECTORREG_ZMM30_BASE,
        VECTORREG_ZMM31_BASE,

        VECTORREG_MICROVP_BASE = VECTORREG_XMM_BASE + NumVectorRegs,
        VECTORREG_MICROVP0 = VECTORREG_MICROVP_BASE,
        VECTORREG_MICROVP1,
        VECTORREG_MICROVP2,
        VECTORREG_MICROVP3,
        VECTORREG_MICROVP4,
        VECTORREG_MICROVP5,
        VECTORREG_MICROVP6,
        VECTORREG_MICROVP7,

        NUM_VECTORREGS = VECTORREG_MICROVP_BASE + NumMicroVectorRegs
    };

    static inline VectorRegIndex
    VECTORREG_XMM(int index)
    {
        return (VectorRegIndex)(VECTORREG_XMM_BASE + index);
    }

    static inline VectorRegIndex
    VECTORREG_XMM2(int index)
    {
        return (VectorRegIndex)(VECTORREG_XMM_BASE + index);
    }

    static inline VectorRegIndex
    VECTORREG_XMM4(int index)
    {
        return (VectorRegIndex)(VECTORREG_XMM_BASE + index);
    }

    static inline VectorRegIndex
    VECTORREG_YMM(int index)
    {
        return (VectorRegIndex)(VECTORREG_YMM_BASE + index);
    }

    static inline VectorRegIndex
    VECTORREG_YMM2(int index)
    {
        return (VectorRegIndex)(VECTORREG_YMM_BASE + index);
    }

    static inline VectorRegIndex
    VECTORREG_YMM4(int index)
    {
        return (VectorRegIndex)(VECTORREG_YMM_BASE + index);
    }

    static inline VectorRegIndex
    VECTORREG_ZMM(int index)
    {
        return (VectorRegIndex)(VECTORREG_ZMM_BASE + index);
    }

    static inline VectorRegIndex
    VECTORREG_ZMM2(int index)
    {
        return (VectorRegIndex)(VECTORREG_ZMM_BASE + index);
    }

    static inline VectorRegIndex
    VECTORREG_ZMM4(int index)
    {
        return (VectorRegIndex)(VECTORREG_ZMM_BASE + index);
    }

    static inline VectorRegIndex
    VECTORREG_MICROVP(int index)
    {
        return (VectorRegIndex)(VECTORREG_MICROVP_BASE + index);
    }

}

#endif // __ARCH_X86_VECTORREGS_HH__
