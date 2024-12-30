import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { useState } from "react"
import { Loader2 } from "lucide-react"
import { useStore } from "@/lib/store"

export function InputWithButton() {
  const [companyName, setCompanyName] = useState<string>('')
  const [isPending, setIsPending] = useState<boolean>(false)
  const companyDataStore = useStore()
  const backendName = import.meta.env.VITE_BACKEND_NAME || 'http://localhost:5000/askVertexAI'
  const [backendUrl, setBackendUrl] = useState<string>('')

  const loggin = async () => {
    try {
      
      console.log(backendName)
  
      const newUrl = 'https://' + backendName + '/askVertexAI'
      console.log(newUrl)
      setBackendUrl(newUrl)
      const response = await fetch(newUrl)
      console.log(response)
    } catch (error) {
      console.error(error)
    }
  }


  const handleSearch = async () => {
    setIsPending(true)
    const response = await fetch(backendUrl, {
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

  const handleKeyPress = async (event: React.KeyboardEvent) => {
    if (event.key === 'Enter') {
      handleSearch(); 
    }
  }

  return (
    <div className="flex w-full max-w-sm items-center space-x-2">
      <Input
        type="text"
        placeholder="What company do you want to look up?"
        value={companyName}
        onChange={(e) => setCompanyName(e.target.value)}
        onKeyDown={handleKeyPress}
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
      <Button
        type="submit"
        onClick={loggin}
        >
        Loggin
      </Button>
    </div>
  )
}
