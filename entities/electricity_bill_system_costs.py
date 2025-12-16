from typing import Optional
import pandas as pd
from pydantic import BaseModel

from common.enums import ConsumerType


class ElectricityBillSystemCosts(BaseModel):
    consumer_type: int
    consumption_kwh: float
    contracted_power_kw: float
    voltage_kv: Optional[float] = None
    # ------ TARIFFE DI RETE in cent/kWh ------
    sigma_1: float = 0
    sigma_2: float = 0
    sigma_3: float = 0
    # ------ FATTORI DI PERDITA in cent/kWh ------
    per_unit_costs: float = 0
    per_kw_costs: float = 0
    per_kwh_costs: float = 0
    # ------ ONERI DI SISTEMA in cent/kWh --------- 
    per_unit_costs_class_0: float = 0
    per_kw_costs_class_0: float = 0
    per_kwh_costs_class_0: float = 0
    per_unit_costs_asos_1: float = 0
    per_kw_costs_asos_1: float = 0
    per_kwh_costs_asos_1: float = 0
    per_unit_costs_asos_2: float = 0
    per_kw_costs_asos_2: float = 0
    per_kwh_costs_asos_2: float = 0
    per_unit_costs_asos_3: float = 0
    per_kw_costs_asos_3: float = 0
    per_kwh_costs_asos_3: float = 0
    per_unit_costs_val: float = 0
    per_kw_costs_val: float = 0
    per_kwh_costs_val: float = 0

    @property
    def consumer_type_enum(self) -> ConsumerType:
        return ConsumerType(self.consumer_type) 
    
    def _get_sigma_1(self) -> float:
        return self.sigma_1 / 100
    
    def _get_per_unit_costs(self) -> float:
        return 0 if self.per_unit_costs is None or pd.isna(self.per_unit_costs) else self.per_unit_costs / 100
    
    def _get_per_unit_costs_class_0(self) -> float:
        return 0 if self.per_unit_costs_class_0 is None or pd.isna(self.per_unit_costs_class_0) else self.per_unit_costs_class_0 / 100

    def _get_per_unit_costs_asos_1(self) -> float:
        return 0 if self.per_unit_costs_asos_1 is None or pd.isna(self.per_unit_costs_asos_1) else self.per_unit_costs_asos_1 / 100

    def _get_per_unit_costs_asos_2(self) -> float:
        return 0 if self.per_unit_costs_asos_2 is None or pd.isna(self.per_unit_costs_asos_2) else self.per_unit_costs_asos_2 / 100

    def _get_per_unit_costs_asos_3(self) -> float:
        return 0 if self.per_unit_costs_asos_3 is None or pd.isna(self.per_unit_costs_asos_3) else self.per_unit_costs_asos_3 / 100

    def _get_per_unit_costs_val(self) -> float:
        return 0 if self.per_unit_costs_val is None or pd.isna(self.per_unit_costs_val) else self.per_unit_costs_val / 100


    def _get_sigma_2(self, contracted_power_kw) -> float:
        return (self.sigma_2 / 100) * contracted_power_kw
    
    def _get_per_kw_costs(self, contracted_power_kw):
        if self.per_kw_costs is None or pd.isna(self.per_kw_costs):
            return 0
        return (self.per_kw_costs / 100) * contracted_power_kw 
    
    def _get_per_kw_costs_class_0(self, contracted_power_kw) -> float:
        if self.per_kw_costs_class_0 is None or pd.isna(self.per_kw_costs_class_0):
            return 0
        return (self.per_kw_costs_class_0 / 100) * contracted_power_kw
    
    def _get_per_kw_costs_asos_1(self, contracted_power_kw) -> float:
        if self.per_kw_costs_asos_1 is None or pd.isna(self.per_kw_costs_asos_1):
            return 0
        return (self.per_kw_costs_asos_1 / 100) * contracted_power_kw

    def _get_per_kw_costs_asos_2(self, contracted_power_kw) -> float:
        if self.per_kw_costs_asos_2 is None or pd.isna(self.per_kw_costs_asos_2):
            return 0
        return (self.per_kw_costs_asos_2 / 100) * contracted_power_kw

    def _get_per_kw_costs_asos_3(self, contracted_power_kw) -> float:
        if self.per_kw_costs_asos_3 is None or pd.isna(self.per_kw_costs_asos_3):
            return 0
        return (self.per_kw_costs_asos_3 / 100) * contracted_power_kw

    def _get_per_kw_costs_val(self, contracted_power_kw) -> float:
        if self.per_kw_costs_val is None or pd.isna(self.per_kw_costs_val):
            return 0
        return (self.per_kw_costs_val / 100) * contracted_power_kw
        

    def _get_sigma_3(self, consumption_kwh) -> float:
        return (self.sigma_3 / 100) * consumption_kwh
    
    def _get_per_kwh_costs(self, consumption_kwh):
        if self.per_kwh_costs is None or pd.isna(self.per_kwh_costs):
            return 0
        return (self.per_kwh_costs / 100) * consumption_kwh 
    
    def _get_per_kwh_costs_class_0(self, consumption_kwh):
        if self.per_kwh_costs_class_0 is None or pd.isna(self.per_kwh_costs_class_0):
            return 0
        return (self.per_kwh_costs_class_0 / 100) * consumption_kwh

    def _get_per_kwh_costs_asos_1(self, consumption_kwh):
        if self.per_kwh_costs_asos_1 is None or pd.isna(self.per_kwh_costs_asos_1):
            return 0
        return (self.per_kwh_costs_asos_1 / 100) * consumption_kwh

    def _get_per_kwh_costs_asos_2(self, consumption_kwh):
        if self.per_kwh_costs_asos_2 is None or pd.isna(self.per_kwh_costs_asos_2):
            return 0
        return (self.per_kwh_costs_asos_2 / 100) * consumption_kwh

    def _get_per_kwh_costs_asos_3(self, consumption_kwh):
        if self.per_kwh_costs_asos_3 is None or pd.isna(self.per_kwh_costs_asos_3):
            return 0
        return (self.per_kwh_costs_asos_3 / 100) * consumption_kwh

    def _get_per_kwh_costs_val(self, consumption_kwh):
        if self.per_kwh_costs_val is None or pd.isna(self.per_kwh_costs_val):
            return 0
        return (self.per_kwh_costs_val / 100) * consumption_kwh


    def calculate_electricity_bill_system_costs( # oneri
        self,
        consumer_type: int,
        consumption_kwh,
        uc3_energy_euro_per_kWh: float,
        uc6_power_euro_per_kWh: float,
        uc6_energy_euro_per_kWh: float,
        contracted_power_kw: float, 
        voltage_kv: Optional[float] = None
    ):
        per_unit_costs = 0
        per_kw_costs = contracted_power_kw * uc6_power_euro_per_kWh
        per_kwh_costs = consumption_kwh * (uc3_energy_euro_per_kWh + uc6_energy_euro_per_kWh)
        
        if consumer_type == 0 or consumer_type == 1: # DOMESTIC
            # ------ TARIFFE DI RETE ------
            per_unit_costs += self._get_sigma_1()
            per_kw_costs += self._get_sigma_2(contracted_power_kw)
            per_kwh_costs += self._get_sigma_3(consumption_kwh)
        else:
            # ------ FATTORI DI PERDITA ------
            per_unit_costs += self._get_per_unit_costs()
            per_kw_costs += self._get_per_kw_costs(contracted_power_kw)
            per_kwh_costs += self._get_per_kwh_costs(consumption_kwh)

        # ------ ONERI DI SISTEMA ---------
        if consumer_type == 0 and contracted_power_kw <= 3: # BT domestico residente
            per_unit_costs += self._get_per_unit_costs_class_0()
            per_kw_costs += self._get_per_kw_costs_class_0(contracted_power_kw)
            per_kwh_costs += self._get_per_kwh_costs_class_0(consumption_kwh)
        elif consumer_type == 1 and contracted_power_kw <= 3: # BT domestico non residente
            per_unit_costs += self._get_per_unit_costs_asos_1()
            per_kw_costs += self._get_per_kw_costs_asos_1(contracted_power_kw)
            per_kwh_costs += self._get_per_kwh_costs_asos_1(consumption_kwh)
        elif (
            (consumer_type in [2, 3]) or # BT non domestiche, illuminazione pubblica, ricarica EV
            (consumer_type== 4 and 0 <= contracted_power_kw <= 10) or
            (consumer_type== 5 and contracted_power_kw <= 100)
        ):
            per_unit_costs += self._get_per_unit_costs_asos_2()
            per_kw_costs += self._get_per_kw_costs_asos_2(contracted_power_kw)
            per_kwh_costs += self._get_per_kwh_costs_asos_2(consumption_kwh)
            
        elif (
            (consumer_type in [6,7] and contracted_power_kw > 500) or # Media/Alta tensione
            (consumer_type == 8 and voltage_kv is not None and voltage_kv < 380)
        ): 
            per_unit_costs += self._get_per_unit_costs_asos_3()
            per_kw_costs += self._get_per_kw_costs_asos_3(contracted_power_kw)
            per_kwh_costs += self._get_per_kwh_costs_asos_3(consumption_kwh)
        elif consumer_type == 8 and voltage_kv is not None and voltage_kv >= 380: # Altissima tensione >=380 kV
            per_unit_costs += self._get_per_unit_costs_val()
            per_kw_costs += self._get_per_kw_costs_val(contracted_power_kw)
            per_kwh_costs += self._get_per_kwh_costs_val(consumption_kwh)

        return per_unit_costs, per_kw_costs, per_kwh_costs
    
