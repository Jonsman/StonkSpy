import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { useState } from "react"
import { Loader2 } from "lucide-react"
import { useStore } from "@/lib/store"

export function InputWithButton() {
  const [companyName, setCompanyName] = useState<string>('')
  const AppStore = useStore()
  // const api = 'api/askVertexAI'
  const API_BASE_URL = import.meta.env.VITE_API_URL || '';
  const api = `${API_BASE_URL}/api/askVertexAI`;

  const handleSearch = async () => {
    AppStore.setIsPendingZustand(true)
    const response = await fetch(api, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ companyName })
    })

    const data = await response.json()
    AppStore.setCompanyData(data)
    AppStore.setIsPendingZustand(false)
  }

  const handleKeyPress = async (event: React.KeyboardEvent) => {
    if (event.key === 'Enter') {
      handleSearch(); 
    }
  }

  return (
    <div className="flex w-full max-w-sm items-center space-x-2">
      <Input
        type="text"
        placeholder="What company do you want to research?"
        value={companyName}
        onChange={(e) => setCompanyName(e.target.value)}
        onKeyDown={handleKeyPress}
      />
      <Button
        type="submit"
        disabled={AppStore.isPendingZustand}
        onClick={handleSearch}
      >
        {AppStore.isPendingZustand ? (
          <>
            <Loader2 className="h-5 w-5 animate-spin" />
            Loading
          </>
        ) : (
          'Search'
        )}
      </Button>
    </div>
  )
}