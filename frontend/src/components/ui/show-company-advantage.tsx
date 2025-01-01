import { useStore } from "@/lib/store"
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"

export function ShowCompanyAdvantage() {
  const AppStore = useStore()

  if (!AppStore.companyData || AppStore.isPendingZustand) {
    return null
  }

  return (
    <Card className="w-1/2">
        <CardHeader>
            <CardTitle>Competitive Advantages</CardTitle>
        </CardHeader>
      <CardContent>
        <div>
          <ul className="list-decimal text-sm">
            {AppStore.companyData?.competitiveAdvantages?.map((advantage, index) => (
              <li className="pb-2.5" key={index}>{advantage}</li>
            )) ?? <li>No competitive advantages available</li>}
          </ul>
        </div>
      </CardContent>
    </Card>
  )
}