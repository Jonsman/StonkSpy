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
  const AppStore = useStore()

  if (!AppStore.companyData || AppStore.isPendingZustand) {
    return null
  }

  return (
    <Card>
      <CardHeader>
        <CardTitle>{AppStore.companyData.companyName}</CardTitle>
        <CardDescription>{String(AppStore.companyData.dateOfData)}</CardDescription>
      </CardHeader>
      <CardContent>
        <div>
          <p>{String(AppStore.companyData.businessDescription)}</p>
        </div>
      </CardContent>
      <CardFooter>
        <p>{String(AppStore.companyData.disclaimer)}</p>
      </CardFooter>
    </Card>
  )
}