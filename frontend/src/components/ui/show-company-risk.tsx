import { useStore } from "@/lib/store"
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"

export function ShowCompanyRisk() {
  const AppStore = useStore()

  if (!AppStore.companyData || AppStore.isPendingZustand) {
    return null
  }

  return (
    <Card className="w-1/2">
        <CardHeader>
            <CardTitle>Investment Risks</CardTitle>
        </CardHeader>
      <CardContent>
        <div>
          <ul className="list-decimal text-sm">
            {AppStore.companyData?.investmentRisks?.map((risk, index) => (
              <li className="pb-2.5" key={index}>{risk}</li>
            )) ?? <li>No investment risks available</li>}
          </ul>
        </div>
      </CardContent>
    </Card>
  )
}