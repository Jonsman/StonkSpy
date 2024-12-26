import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { useState } from "react"
import { Loader2 } from "lucide-react"
import { useStore } from "@/lib/store"



export function InputWithButton() {
  const [companyName, setCompanyName] = useState<string>('')
  const [isPending, setIsPending] = useState<boolean>(false)
  const companyDataStore = useStore()
  const apiUrl = import.meta.env.VITE_API_URL;

  console.log('apiUrl', apiUrl)
  console.log('apiUrlEnv', import.meta.env.VITE_API_URL)

  const handleSearch = async () => {
    setIsPending(true)
    const response = await fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ companyName })
    })

    const data = await response.json()
    companyDataStore.setCompanyData(data)
    setIsPending(false)
  }

  return (
    <div className="flex w-full max-w-sm items-center space-x-2">
      <Input
        type="text"
        placeholder="What company do you want to look up?"
        value={companyName}
        onChange={(e) => setCompanyName(e.target.value)}
      />
      <Button
        type="submit"
        disabled={isPending}
        onClick={handleSearch}
      >
        {isPending ? (
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
