/*
 * Copyright (c) 2009 The Regents of The University of Michigan
 * All rights reserved.
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
 */

#ifndef __ARCH_X86_ISA_HH__
#define __ARCH_X86_ISA_HH__

#include <iostream>
#include <string>

#include "arch/generic/isa.hh"
#include "arch/x86/registers.hh"
#include "arch/x86/regs/float.hh"
#include "arch/x86/regs/misc.hh"
#include "base/types.hh"
#include "cpu/reg_class.hh"
#include "sim/sim_object.hh"

class Checkpoint;
class EventManager;
class ThreadContext;
struct X86ISAParams;

namespace X86ISA
{
    class ISA : public BaseISA
    {
      protected:
        RegVal regVal[NUM_MISCREGS];
        void updateHandyM5Reg(Efer efer, CR0 cr0,
                SegAttr csAttr, SegAttr ssAttr, RFLAGS rflags);

      public:
        void clear();

        typedef X86ISAParams Params;

        ISA(Params *p);
        const Params *params() const;

        RegVal readMiscRegNoEffect(int miscReg) const;
        RegVal readMiscReg(int miscReg);

        void setMiscRegNoEffect(int miscReg, RegVal val);
        void setMiscReg(int miscReg, RegVal val);

        RegId
        flattenRegId(const RegId& regId) const
        {
            switch (regId.classValue()) {
              case IntRegClass:
                return RegId(IntRegClass, flattenIntIndex(regId.index()));
              case FloatRegClass:
                return RegId(FloatRegClass, flattenFloatIndex(regId.index()));
              case VecRegClass:
                return RegId(VecRegClass, flattenVecIndex(regId.index()));
              case OpMaskRegClass:
                return RegId(OpMaskRegClass, flattenOpMaskIndex(regId.index()));
              case CCRegClass:
                return RegId(CCRegClass, flattenCCIndex(regId.index()));
              case MiscRegClass:
                return RegId(MiscRegClass, flattenMiscIndex(regId.index()));
              default:
                break;
            }
            return regId;
        }

        int flattenIntIndex(int reg) const { return reg & ~IntFoldBit; }

        int
        flattenFloatIndex(int reg) const
        {
            if (reg >= NUM_FLOATREGS) {
                reg = FLOATREG_STACK(reg - NUM_FLOATREGS,
                                     regVal[MISCREG_X87_TOP]);
            }
            return reg;
        }

        int flattenVecIndex(int reg) const { return reg; }
        int flattenVecElemIndex(int reg) const { return reg; }
        int flattenVecPredIndex(int reg) const { return reg; }
        int flattenOpMaskIndex(int reg) const { return reg; }
        int flattenCCIndex(int reg) const { return reg; }
        int flattenMiscIndex(int reg) const { return reg; }

        void serialize(CheckpointOut &cp) const override;
        void unserialize(CheckpointIn &cp) override;

        void setThreadContext(ThreadContext *_tc) override;
    };
}

#endif
