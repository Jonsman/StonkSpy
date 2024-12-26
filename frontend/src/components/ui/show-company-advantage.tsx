import { useStore } from "@/lib/store"
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"

export function ShowCompanyAdvantage() {
  const companyDataStore = useStore()

  if (!companyDataStore.companyData) {
    return null
  }
  
console.log(companyDataStore.companyData)

  return (
    <Card>
        <CardHeader>
            <CardTitle>Competitive Advantages</CardTitle>
        </CardHeader>
      <CardContent>
        <div>
          <ul className="list-decimal text-sm">
            {companyDataStore.companyData?.competitiveAdvantages?.map((advantage, index) => (
              <li className="pb-2.5" key={index}>{advantage}</li>
            )) ?? <li>No competitive advantages available</li>}
          </ul>
        </div>
      </CardContent>
    </Card>
  )
}