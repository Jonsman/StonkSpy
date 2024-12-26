import { create } from "zustand";

export interface CompanyData {
    companyName: string | null;
    dateOfData: string | null;
    businessDescription: string | null;
    competitiveAdvantages: string[];
    investmentRisks: string[];
    disclaimer: string | null;
  }

export interface CompanyStore {
    companyData: CompanyData | null;
    setCompanyData: (data: CompanyData) => void;
  }

// Zustand store
export const useStore = create<CompanyStore>((set) => ({
    companyData: null,
    setCompanyData: (companyData: any) => set({ companyData }),
  }))