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
        <CardDescription>{AppStore.companyData.dateOfData}</CardDescription>
      </CardHeader>
      <CardContent>
        <div>
          <p>{AppStore.companyData.businessDescription}</p>
        </div>
      </CardContent>
      <CardFooter>
        <p>{AppStore.companyData.disclaimer}</p>
      </CardFooter>
    </Card>
  )
}