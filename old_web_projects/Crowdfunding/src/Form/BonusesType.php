<?php

namespace App\Form;

use App\Entity\Bonuses;
use Symfony\Component\Form\AbstractType;
use Symfony\Component\Form\Extension\Core\Type\IntegerType;
use Symfony\Component\Form\Extension\Core\Type\TextType;
use Symfony\Component\Form\FormBuilderInterface;
use Symfony\Component\OptionsResolver\OptionsResolver;

class BonusesType extends AbstractType
{
    public function buildForm(FormBuilderInterface $builder, array $options)
    {
        $builder
            ->add('name', TextType::class, [
                'label' => false,
                'attr' => ['placeholder' => 'Name'],
            ])
            ->add('money', IntegerType::class, [
                'label' => false,
                'attr' => ['placeholder' => 'Money'],
            ])
            ->add('description', TextType::class, [
                'label' => false,
                'attr' => ['placeholder' => 'Description'],
            ])
        ;
    }

    public function configureOptions(OptionsResolver $resolver)
    {
        $resolver->setDefaults([
            'data_class' => Bonuses::class,
        ]);
    }
}
