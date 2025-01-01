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
      <div className="flex py-4 gap-4 items-center justify-center fixed bottom-0 left-1/2 -translate-x-1/2">
        <a href="https://github.com/Jonsman" target="_blank" className="flex text-xs gap-2">
        <img
          src="/GitHub_Invertocat_Light.svg"
          alt="GitHub"
          className="h-5 w-5 dark:hidden"
        />
        <img
          src="/GitHub_Invertocat_Dark.svg"
          alt="GitHub"
          className="h-5 w-5 hidden dark:block"
        />
        by Jonsman
        </a>
      </div>
    </ThemeProvider>
  );
}

export default App
