import { useStore } from "@/lib/store"
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"

export function ShowCompanyRisk() {
  const companyDataStore = useStore()

  if (!companyDataStore.companyData) {
    return null
  }
console.log(companyDataStore.companyData)

  return (
    <Card>
        <CardHeader>
            <CardTitle>Investment Risks</CardTitle>
        </CardHeader>
      <CardContent>
        <div>
          <ul className="list-decimal text-sm">
            {companyDataStore.companyData?.investmentRisks?.map((risk, index) => (
              <li className="pb-2.5" key={index}>{risk}</li>
            )) ?? <li>No competitive advantages available</li>}
          </ul>
        </div>
      </CardContent>
    </Card>
  )
}