import { InputWithButton } from '@/components/ui/input-with-button'
import './App.css'
import { ThemeProvider } from '@/components/ui/theme-provider';
import { ModeToggle } from '@/components/ui/mode-toggle';
import { ShowCompanyBusiness } from '@/components/ui/show-company-business';
import { ShowCompanyAdvantage } from '@/components/ui/show-company-advantage';
import { ShowCompanyRisk } from '@/components/ui/show-company-risk';
import { Skeleton } from '@/components/ui/skeleton';
import { useStore } from "@/lib/store"

function App() {
  const AppStore = useStore()

  return (
    <ThemeProvider defaultTheme="system" storageKey="vite-ui-theme">
      <div className="flex flex-col py-4 gap-4 items-center justify-center min-h-screen"> 
        <div className="absolute top-4 right-4">
          <ModeToggle />
        </div>
        <InputWithButton />
        { AppStore.isPendingZustand && <Skeleton className="space-x-2 h-60 w-full" /> }
        <ShowCompanyBusiness />
        <div className="flex flex-row gap-4 w-full">
          { AppStore.isPendingZustand && <Skeleton className="h-80 w-1/2" /> }
          { AppStore.isPendingZustand && <Skeleton className="h-80 w-1/2" /> }
          <ShowCompanyAdvantage />
          <ShowCompanyRisk />
        </div>
      </div>
    </ThemeProvider>
  );
}

export default App
