import { create } from "zustand";

export interface CompanyData {
    companyName: string | null;
    dateOfData: string | null;
    businessDescription: string | null;
    competitiveAdvantages: string[];
    investmentRisks: string[];
    disclaimer: string | null;
  }

export interface AppStore {
    companyData: CompanyData | null;
    isPendingZustand: boolean;
    setCompanyData: (data: CompanyData) => void;
    setIsPendingZustand: (isPending: boolean) => void;
  }

// Zustand store
export const useStore = create<AppStore>((set) => ({
    companyData: null,
    isPendingZustand: false,
    setCompanyData: (companyData: any) => set({ companyData }),
    setIsPendingZustand: (isPendingZustand: boolean) => set({ isPendingZustand }),
  }))