import { useStore } from "@/lib/store"
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"

export function ShowCompanyBusiness() {
  const companyDataStore = useStore()

  if (!companyDataStore.companyData) {
    return null
  }
console.log(companyDataStore.companyData)

  return (
    <Card>
      <CardHeader>
        <CardTitle>{companyDataStore.companyData.companyName}</CardTitle>
        <CardDescription>{companyDataStore.companyData.dateOfData}</CardDescription>
      </CardHeader>
      <CardContent>
        <div>
          <p>{companyDataStore.companyData.businessDescription}</p>
        </div>
      </CardContent>
      <CardFooter>
        <p>{companyDataStore.companyData.disclaimer}</p>
      </CardFooter>
    </Card>
  )
}